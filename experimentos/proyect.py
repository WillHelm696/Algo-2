import argparse
import os
import pickle
import time
from sklearn.feature_extraction.text 
import TfidfVectorizer

def create_document_db(path):
    # Inicializar base de datos de documentos
    document_db = {}

    # Cargar archivos desde el directorio especificado
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        with open(file_path, 'r') as f:
            # Almacenar el contenido del archivo como título del documento
            title = file
            # Almacenar el contenido del archivo como contenido del documento
            content = f.read()

        # Agregar documento a la base de datos
        document_db[title] = content

    # Guardar la base de datos de documentos en un archivo
    with open('document_db.pkl', 'wb') as f:
        pickle.dump(document_db, f)

def search_documents(query):
    # Cargar base de datos de documentos
    with open('document_db.pkl', 'rb') as f:
        document_db = pickle.load(f)

    # Cree un vectorizador para convertir el contenido de la consulta y el documento en una representación vectorial
    vectorizer = TfidfVectorizer()

    # Transformar la consulta a una representación vectorial.
    query_vector = vectorizer.fit_transform([query])

    # Calcule las puntuaciones de similitud entre la consulta y cada documento en la base de datos.
    similarity_scores = []
    for title, content in document_db.items():
        # Transforme el contenido del documento a una representación vectorial.
        document_vector = vectorizer.transform([content])
        # Calcule la similitud del coseno entre los vectores de consulta y documento.
        similarity_score = cosine_similarity(query_vector, document_vector)
        # Almacene la puntuación de similitud junto con el título del documento.
        similarity_scores.append((similarity_score, title))

    # Ordenar las puntuaciones de similitud en orden descendente
    sorted_similarity_scores = sorted(similarity_scores, key=lambda x: x[0], reverse=True)

    # imprimir los resultados
    for similarity_score, title in sorted_similarity_scores:
        print(f"Title: {title}")
        print(f"Similarity Score: {similarity_score}")
        print("-------------------")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-create', '--create_document_db', type=str, help='Create a document database')
    parser.add_argument('-search', '--search_documents', type=str, help='Search documents in the document database')
    args = parser.parse_args()

    if args.create_document_db:
        create_document_db(args.create_document_db)
    elif args.search_documents:
        search_documents(args.search_documents)
    else:
        print("Invalid arguments. Use --help for usage information.")
