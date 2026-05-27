import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc
import numpy as np
import streamlit as st

# Função de fibonacci em função iterativa com n como termo
def fibonacci_iterative(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence[:n]

# Desenha o número de fibonacci com a lista de números

def plot_fibonacci(sequence: list[int]) -> None:
    golden_ratio = sequence[-1] / sequence[-2]
    
    angles = np.linspace(0, 8 * np.pi, num=len(sequence))

    radius = golden_ratio ** (angles / np.pi)

    x = radius * np.cos(angles)
    y = radius * np.sin(angles)


    plt.figure(figsize=(8, 8))
    plt.plot(x, y, color="black", linewidth=2)
    plt.axis("equal")
    plt.axis("off")
    return plt

# Função start

def main():
    st.title("Fibonacci") 
    st.set_page_config( 
                       page_title="Fibonacci", 
                       layout="wide" 
                       ) 
    col1, col2 = st.columns([1, 1]) 
    with col1: 
        st.subheader("Gerador") 
        length = st.number_input( 
                                 "Insira um número inteiro positivo:", 
                                 min_value=3, 
                                 max_value=20000, 
                                 step=1 
                                 ) 
        if st.button("Criar sequência"): 
            sequence = fibonacci_iterative(length) 
            st.session_state["sequence"] = sequence 
            st.session_state["generated"] = True 
            st.success("Sequência gerada!") 
            st.write(sequence) 
            plot = plot_fibonacci(sequence) 
            st.pyplot(plot) 
    with col2: 
        st.subheader("Procurar na sequência") 
        if st.session_state.get("generated", False): 
            number_search = st.number_input( 
                                            "Digite o índice do termo:", 
                                            min_value=0, 
                                            step=1, 
                                            key="search" 
            )
            sequence = st.session_state["sequence"] 
            if number_search < len(sequence): 
                st.metric( 
                          label=f"Termo {number_search}", 
                          value=sequence[number_search], 
                ) 
            else: 
                st.error("Índice fora do intervalo!")

if __name__ == "__main__":
    main()
