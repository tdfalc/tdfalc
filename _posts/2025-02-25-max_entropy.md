---
title: Maximum Entropy Principle
subtitle: "Why do we always use the Gaussian distribution in statistical modelling?"
layout: nocode
date: 2025-02-25
keywords: statistics
published: true
---

The [Gaussian distribution](https://en.wikipedia.org/wiki/Normal_distribution) is popular in statistics not only because of its mathematical convenience and its role in the [central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)—which states that the sum of many independent variables tends to be normally distributed—but also due to its maximum entropy property. According to the maximum entropy principle, if the only information available about a dataset is its mean and variance, the best choice is the distribution that maximizes entropy under these constraints. In other words, among all distributions with a specified mean and variance, the normal distribution introduces the fewest additional assumptions, making it the most unbiased and uninformative model. This lack of extra structure is a key reason for its widespread use in statistical inference and information theory. In this post, we derive the Gaussian distribution from the fundamental principles of information theory to illustrate this concept.

## Entropy
Let {% katexmm %} $X$ {% endkatexmm %} be a random variable with a probability density function {% katexmm %} $f$ {% endkatexmm %} whose support is a set {% katexmm %} $\mathcal{X}$ {% endkatexmm %}. The entropy of this random variable is given by

{% katexmm %}
$$
\begin{aligned}
H(X) = - \int_{\mathcal{X}} f(x) \log f(x) dx = \mathbb{E}_{\mathcal{X}} \left[\log \frac{1}{f(x)}\right],
\end{aligned}
$$
{% endkatexmm %}

which can be thought of as the average amount of information gained from observing an outcome drawn from a probability distribution. Essentially, it measures the uncertainty associated with the possible outcomes of a random variable. For a more detailed and intuitive explanation, there's an excellent blog post [here](https://alexkritchevsky.com/2018/02/23/entropy-1.html) on the topic.

## Maximizing Entropy

The [principle of maximum entropy](https://en.wikipedia.org/wiki/Principle_of_maximum_entropy) states that, among all distributions that satisfy our prior constraints, the one with the highest entropy is favored because it makes the fewest additional assumptions. In essence, it embraces "epistemic modesty" or "maximum ignorance", ensuring that only the provided information is encoded, while remaining as non-committal as possible about what is unknown. For a given mean and variance, the maximum entropy probability distribution {% katexmm %} $f^\ast$ {% endkatexmm %} is given by

{% katexmm %}
$$
\begin{aligned}
f^\ast = \argmin_{f} & \int_{\mathcal{X}} f(x) \log f(x) dx, \\
\textrm{s.t.} \quad & \int_{\mathcal{X}} f(x) dx = 1, \\
& \int_{\mathcal{X}} f(x) (x - \mu)^2 dx = \sigma^2, \\
\end{aligned}
$$
{% endkatexmm %}

where the first constraint simply ensures the distribution is a probability density function and the second constraint defines the variance, which gives us the mean by default. To solve this, we can use the method of Lagrange multipliers such that the Lagrangian is

{% katexmm %}
$$
\begin{aligned}
\mathcal{J}(f, \boldsymbol{\lambda}) = \int_{\mathcal{X}} f(x) \log f(x) dx - \lambda_1 \left( \int_{\mathcal{X}} f(x) dx - 1 \right) - \lambda_2 \left( \int_{\mathcal{X}} f(x) (x - \mu)^2 dx - \sigma^2 \right).
\end{aligned}
$$
{% endkatexmm %}

Taking the derivative with respect to {% katexmm %} $f$ {% endkatexmm %} and setting this to zero we get

{% katexmm %}
$$
\begin{aligned}
\frac{d}{df}\mathcal{J}(f, \boldsymbol{\lambda}) &= 1 + \log f(x) - \lambda_1  - \lambda_2 (x - \mu)^2 = 0, \\
\therefore f(x) &= \exp\left( -\lambda_1 + 1 - \lambda_2 (x - \mu)^2 \right).
\end{aligned}
$$
{% endkatexmm %}

Therefore, to satisfy the first constraint the following must hold

{% katexmm %}
$$
\begin{aligned}
1 &= \int_{\mathcal{X}} \exp\left( -\lambda_1 + 1 - \lambda_2 (x - \mu)^2 \right) dx, \\
1 &= \int_{\mathcal{X}} \exp\left( -\lambda_1 + 1 \right) \exp\left( - \lambda_2 (x - \mu)^2 \right) dx, \\
\therefore \exp\left( \lambda_1 - 1 \right) &= \int_{\mathcal{X}} \exp\left( - \lambda_2 (x - \mu)^2 \right) dx.
\end{aligned}
$$
{% endkatexmm %}

We can solve the right-hand side by substitution, setting {% katexmm %} $u = x - \mu$ {% endkatexmm %}. This shifts the variable of integration without affecting the limits so the integral becomes a standard [Euler–Poisson integral](https://en.wikipedia.org/wiki/Gaussian_integral) with the well-known result

{% katexmm %}
$$
\begin{aligned}
\int_{\mathcal{X}} \exp\left( -\lambda_2 u^2 \right) du = \sqrt{\frac{\pi}{\lambda_2}}.
\end{aligned}
$$
{% endkatexmm %}

To satisfy the second constraint, the following must hold

{% katexmm %}
$$
\begin{aligned}
\sigma^2 &= \int_{\mathcal{X}} \exp \left( -\lambda_1 + 1 - \lambda_2 (x - \mu)^2 \right) (x - \mu)^2 dx, \\
\therefore \sigma^2 \exp \left( \lambda_1 - 1 \right) &= \int_{\mathcal{X}} \exp \left( - \lambda_2 (x - \mu)^2 \right) (x - \mu)^2 dx,
\end{aligned}
$$
{% endkatexmm %}

where again by setting {% katexmm %} $u = x - \mu$ {% endkatexmm %}, the integral on the right-hand side has a [well-known result](https://en.wikipedia.org/wiki/Gaussian_integral#Integrals_of_similar_form) such that

{% katexmm %}
$$
\begin{aligned}
\int_{\mathcal{X}} \exp\left( -\lambda_2 u^2 \right) u^2 du = \frac{1}{2 \lambda_2} \sqrt{\frac{\pi}{\lambda_2}}.
\end{aligned}
$$
{% endkatexmm %}

Therefore, by putting this altogether we get that

{% katexmm %}
$$
\begin{aligned}
\sqrt{\frac{\pi}{\lambda_2}} = \exp\left( \lambda_1 - 1 \right) &= 2 \lambda_2 \sigma^2 \exp\left( \lambda_1 - 1 \right),
\end{aligned}
$$
{% endkatexmm %}

and so by solving first for {% katexmm %} $\lambda_2$ {% endkatexmm %} and substituting the result, we get that 

{% katexmm %}
$$
\begin{aligned}
\lambda_2 &= \frac{1}{2 \sigma^2} \quad \textrm{and} \quad \lambda_1 = \log \sqrt{2 \pi \sigma^2} + 1,
\end{aligned}
$$
{% endkatexmm %}

and finally 

{% katexmm %}
$$
\begin{aligned}
f^\ast(x) &= \exp \left(-\lambda_1 + 1 - \lambda_2 (x - \mu)^2 \right), \\
&= \exp \left(- \log \sqrt{2 \pi \sigma^2}  - \frac{1}{2 \sigma^2}(x - \mu)^2 \right), \\
&= \frac{1}{\sqrt{2 \pi \sigma^2} } \exp \left( -\frac{1}{2 \sigma^2}(x - \mu)^2 \right) 
\end{aligned}
$$
{% endkatexmm %}

which is, of course, the probability density function of the Gaussian distribution. Therefore, for a fixed mean and variance, the Gaussian dsitribution is the maximum entropy distribution, making it the natural choice for statistical modelling.
