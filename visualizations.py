import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração visual padrão
sns.set_theme(style="whitegrid")


def plot_heatmap_with_path(dp_matrix, path, filename="heatmap_dp.png"):
    """Gera o Mapa de Calor da Tabela DP com o caminho ótimo destacado."""
    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(dp_matrix, annot=True, cmap="YlOrRd", cbar_kws={'label': 'Custo Acumulado'})

    # Destaca o caminho ótimo
    y_coords, x_coords = zip(*path)
    ax.plot([x + 0.5 for x in x_coords], [y + 0.5 for y in y_coords],
            marker='o', color='blue', linewidth=3, markersize=8, label='Caminho Ótimo')

    plt.title("Mapa de Calor (DP) e Caminho Ótimo")
    plt.xlabel("Coordenada M (Colunas)")
    plt.ylabel("Coordenada N (Linhas)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


def plot_monte_carlo_distribution(costs, filename="monte_carlo_dist.png"):
    """Gera o Histograma + Boxplot da distribuição Monte Carlo."""
    fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)}, figsize=(8, 6))

    sns.boxplot(x=costs, ax=ax_box, color="lightblue")
    sns.histplot(x=costs, ax=ax_hist, kde=True, bins=30, color="steelblue")

    ax_box.set(yticks=[])
    ax_box.set(xlabel='')
    ax_hist.set_xlabel('Custo Ótimo Simulado')
    ax_hist.set_ylabel('Frequência')
    fig.suptitle('Distribuição de Custos - Simulação Monte Carlo (K=10.000)')

    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


def plot_scalability_curve(sizes, time_fb, time_dp, time_mc, filename="scalability.png"):
    """Curva empírica de tempo de execução vs Tamanho da Instância."""
    plt.figure(figsize=(8, 6))

    plt.plot(sizes[:len(time_fb)], time_fb, marker='o', label='Força Bruta', linestyle='--')
    plt.plot(sizes, time_dp, marker='s', label='Programação Dinâmica')
    plt.plot(sizes, time_mc, marker='^', label='Monte Carlo (K=10.000)')

    plt.yscale('log')  # Escala logarítmica é vital devido à Força Bruta exponencial
    plt.title("Curva de Escalabilidade Empírica (Tempo x Tamanho N=M)")
    plt.xlabel("Tamanho da Grade (N)")
    plt.ylabel("Tempo de Execução (ms) - Escala Log")
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


def plot_sensitivity_analysis(base_costs, minus_20_costs, plus_20_costs, filename="sensitivity.png"):
    """Gráfico comparativo de sensibilidade (p +/- 20%)."""
    plt.figure(figsize=(8, 6))

    sns.kdeplot(base_costs, label="Base (p histórico)", fill=True)
    sns.kdeplot(minus_20_costs, label="Risco Reduzido (p - 20%)", fill=True)
    sns.kdeplot(plus_20_costs, label="Risco Elevado (p + 20%)", fill=True)

    plt.title("Análise de Sensibilidade: Variação de Risco Agroclimático")
    plt.xlabel("Custo Ótimo")
    plt.ylabel("Densidade")
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


def plot_tradeoff_scatter(algos, times, costs, filename="tradeoff.png"):
    """Gráfico de dispersão Custo Ótimo x Tempo Computacional."""
    plt.figure(figsize=(8, 6))

    colors = ['red', 'green', 'blue']
    for i, algo in enumerate(algos):
        plt.scatter(times[i], costs[i], label=algo, color=colors[i], s=100)

    plt.title("Trade-off: Tempo Computacional vs Qualidade (Custo)")
    plt.xlabel("Tempo de Execução (ms)")
    plt.ylabel("Custo Ótimo Calculado")
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


if __name__ == "__main__":
    print("Gerando visualizações obrigatórias...")

    # 1. Mock Data para Heatmap
    dp_mock = np.random.randint(10, 50, size=(5, 5))
    path_mock = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]
    plot_heatmap_with_path(dp_mock, path_mock)

    # 2. Mock Data para Monte Carlo
    mc_costs_mock = np.random.normal(loc=150, scale=15, size=10000)
    plot_monte_carlo_distribution(mc_costs_mock)

    # 3. Mock Data para Escalabilidade
    sizes = [3, 5, 10, 20, 50]
    t_fb = [1, 15, np.nan, np.nan, np.nan]  # Estoura depois de 5
    t_dp = [0.1, 0.2, 0.5, 1.5, 6.0]
    t_mc = [1000, 2000, 5000, 15000, 60000]
    plot_scalability_curve(sizes, t_fb, t_dp, t_mc)

    # 4. Mock Data para Sensibilidade
    mc_base = np.random.normal(150, 15, 10000)
    mc_minus = np.random.normal(120, 12, 10000)
    mc_plus = np.random.normal(180, 18, 10000)
    plot_sensitivity_analysis(mc_base, mc_minus, mc_plus)

    # 5. Mock Data para Tradeoff
    plot_tradeoff_scatter(
        ["Força Bruta (N=5)", "Prog. Dinâmica (N=50)", "Monte Carlo (N=50)"],
        [15, 6.0, 60000],
        [145, 145, 150]
    )

    print("Figuras salvas com sucesso no diretório atual!")