from typing import List


def bayes_source(prior_probs: List[float], conversion_rates: List[float]) -> List[float]:
    """
    Calculates the posterior probabilities of traffic sources after a conversion event
    using Bayes' Theorem.

    Args:
        prior_probs: A list of prior probabilities for each source (sum should be 1.0).
        conversion_rates: A list of conversion rates (likelihoods) for each source.

    Returns:
        A list of posterior probabilities for each source.
    """

    # Validate inputs have the same length
    if len(prior_probs) != len(conversion_rates):
        raise ValueError("Input lists must have the same length.")

    # 1. Calculate the numerator for each source: P(A|Hi) * P(Hi)
    # This represents the joint probability P(A and Hi)
    joint_probs = [p * c for p, c in zip(prior_probs, conversion_rates)]

    # 2. Calculate Total Probability P(A) (The Evidence)
    # This is the sum of all joint probabilities
    total_prob_purchase = sum(joint_probs)

    # Handle edge case where total probability is 0 to avoid division by zero
    if total_prob_purchase == 0:
        return [0.0] * len(prior_probs)

    # 3. Calculate Posterior Probabilities: P(Hi|A) = P(A and Hi) / P(A)
    posterior_probs = [joint / total_prob_purchase for joint in joint_probs]

    return posterior_probs


# --- Testing with the problem data ---
if __name__ == "__main__":
    # Data from the problem
    priors = [0.50, 0.30, 0.20]  # Search, Social, Email
    conversions = [0.04, 0.02, 0.08]

    # Calculate posteriors
    results = bayes_source(priors, conversions)

    # Output results
    sources = ["Search Ads", "Social Media", "Email Marketing"]

    print(f"{'Source':<20} | {'Prior':<10} | {'Conversion':<10} | {'Posterior (Result)':<10}")
    print("-" * 65)

    for i, source in enumerate(sources):
        print(f"{source:<20} | {priors[i]:<10.2f} | {conversions[i]:<10.2f} | {results[i]:.5f}")

    print("-" * 65)
    print(f"Total Probability of Purchase: {sum([p * c for p, c in zip(priors, conversions)]):.3f}")