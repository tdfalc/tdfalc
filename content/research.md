# Research

## Mechanism Design for Trading Information

[Falconer, T., Kazempour, J., & Pinson, P. (2024). *Trading Information in Games*. (Work in progress).]()

## Collaborative Machine Learning

[Falconer, T., Kazempour, J., & Pinson, P. (2024). *Bayesian Regression Markets*. Journal of Machine Learning Research, 25 (180), 1–38.](https://www.jmlr.org/papers/v25/23-1385.html)

**Absract**: Although machine learning tasks are highly sensitive to the quality of input data, relevant datasets can often be challenging for firms to acquire, especially when held privately by a variety of owners. For instance, if these owners are competitors in a downstream market, they may be reluctant to share information. Focusing on supervised learning for regression tasks, we develop a regression market to provide a monetary incentive for data sharing. Our mechanism adopts a Bayesian framework, allowing us to consider a more general class of regression tasks. We present a thorough exploration of the market properties, and show that similar proposals in literature expose the market agents to sizeable financial risks, which can be mitigated in our setup.

[Falconer, T., Kazempour, J., & Pinson, P. (2024). *Towards Replication-Robust Analytics Markets*. arXiv Preprint (Under Review).](https://arxiv.org/abs/2310.06000)

**Abstract**: Despite the widespread use of machine learning throughout industry, many firms face a common challenge: relevant datasets are typically distributed amongst market competitors that are reluctant to share information. Recent works propose analytics markets as a way to provide monetary incentives for data sharing, however many designs are vulnerable to malicious forms of replication, where agents replicate their data and act under false identities to increase revenue, and in turn diminish that of others. Accordingly, we develop a replication-robust analytics market for supervised learning problems. To allocate revenue, we treat features of agents as players and their interactions as a characteristic function game. We show that there are several different ways to describe such a game, each having causal nuances that impact robustness to replication. Our methodology is validated using a real-world wind power forecasting case study.

## Machine Learning for Power Systems Operations

[Falconer, T. & and Mones, L. (2023). *Leveraging Power Grid Topology in Machine Learning Assisted Optimal Power Flow*. IEEE Transactions on Power Systems, 38 (3), 2234-2246](https://ieeexplore.ieee.org/abstract/document/9810496)

**Abstract**: Machine learning assisted optimal power flow (OPF) aims to reduce the computational complexity of these non-linear and non-convex constrained optimization problems by consigning expensive (online) optimization to offline training. The majority of work in this area typically employs fully connected neural networks (FCNN). However, recently convolutional (CNN) and graph (GNN) neural networks have also been investigated, in effort to exploit topological information within the power grid. Although promising results have been obtained, there lacks a systematic comparison between these architectures throughout literature. Accordingly, we introduce a concise framework for generalizing methods for machine learning assisted OPF and assess the performance of a variety of FCNN, CNN and GNN models for two fundamental approaches in this domain: regression (predicting optimal generator set-points) and classification (predicting the active set of constraints). For several synthetic power grids with interconnected utilities, we show that locality properties between feature and target variables are scarce and subsequently demonstrate marginal utility of applying CNN and GNN architectures compared to FCNN for a fixed grid topology. However, with variable topology (for instance, modeling transmission line contingency), GNN models are able to straightforwardly take the change of topological information into account and outperform both FCNN and CNN models.
