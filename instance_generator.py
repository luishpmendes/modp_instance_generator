import osmnx as ox
import pandas as pd
import os

INSTANCE_DIR = "./instance/"
IMAGE_DIR = "./img/"
NUM_DISTRICTS = [5, 10, 20]
PLACES_FILE_PATH = "places.csv"

def process_row(row):
    try:
        print(f"Processing {row['query']}")

        # Create a graph from the place
        G = ox.graph_from_place(row['query'], network_type='drive', simplify=True, retain_all=False)
        save_instance(G, row['name'])
        save_figure(G, row['name'])
      
    except Exception as e:
        print(f"Error processing {row['query']}: {e}")

def save_instance(G, place_name):
    print(f"Saving {place_name}")
    for k in NUM_DISTRICTS:
        filename = os.path.join(INSTANCE_DIR, f"{place_name}_{k}.txt")
        try:
            with open(filename, 'w') as f:
                write_graph_data(G, k, f)
        except IOError as e:
            print(f"Error saving file {filename}: {e}")

def write_graph_data(G, district_count, file):
    num_vertices = len(G.nodes)
    num_edges = len(G.edges)
    file.write(f"{num_vertices} {num_edges} {district_count}\n")
              
    for node, data in G.nodes(data=True):
        file.write(f"{node} {data['x']} {data['y']}\n")

    for edge in G.edges(data=True):
        u, v, data = edge
        distance = data['length'] if 'length' in data else data['length_km'] * 1000
        file.write(f"{u} {v} {distance}\n")

def save_figure(G, place_name):
    filename = os.path.join(IMAGE_DIR, f"{place_name}.png")
    try:
        # Plot the graph
        ox.plot_graph(G, node_size=2, show=False, close=True, save=True, filepath=filename)
    except Exception as e:
        print(f"Error saving figure {filename}: {e}")

def main():
    # Load the data from the CSV file
    places_df = pd.read_csv(PLACES_FILE_PATH)
    for idx, row in places_df.iterrows():
        process_row(row)

if __name__ == "__main__":
    main()
