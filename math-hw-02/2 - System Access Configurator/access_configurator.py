import itertools


def check_access(is_employee, is_verified, is_premium, is_admin, is_banned):
    """
    Determines access rights based on user parameters.

    Logic:
    - Base: Employee AND Verified AND NOT Banned
    - Premium: (Employee OR Premium) AND Verified AND NOT Banned
    - Admin: Admin AND Verified AND NOT Banned
    - Secret: (Admin OR (Employee AND Premium)) AND Verified AND NOT Banned
    """

    # Common condition for all levels: User must be verified and not banned
    is_active = is_verified and not is_banned

    access_rights = {
        'Base': is_employee and is_active,
        'Premium': (is_employee or is_premium) and is_active,
        'Admin': is_admin and is_active,
        'Secret': (is_admin or (is_employee and is_premium)) and is_active
    }

    return access_rights


def main():
    # 2. Generate Truth Table for all 32 combinations (2^5)
    # Using itertools.product as requested
    inputs = list(itertools.product([True, False], repeat=5))

    # Headers
    print(f"{'Emp':<5} {'Ver':<5} {'Prem':<5} {'Adm':<5} {'Ban':<5} | {'Base':<5} {'Prem':<5} {'Adm':<5} {'Secr':<5}")
    print("-" * 65)

    full_access_count = 0
    premium_no_base_cases = []

    for params in inputs:
        is_emp, is_ver, is_prem, is_adm, is_ban = params

        # Get access dictionary
        result = check_access(is_emp, is_ver, is_prem, is_adm, is_ban)

        # 3. Print table row (converting boolean to integer 1/0 for readability)
        input_str = f"{int(is_emp):<5} {int(is_ver):<5} {int(is_prem):<5} {int(is_adm):<5} {int(is_ban):<5}"
        output_str = f"{int(result['Base']):<5} {int(result['Premium']):<5} {int(result['Admin']):<5} {int(result['Secret']):<5}"
        print(f"{input_str} | {output_str}")

        # 4. Data Analysis

        # Count cases with Full Access (all 4 sections are True)
        if all(result.values()):
            full_access_count += 1

        # Check for Premium but NO Base access
        if result['Premium'] and not result['Base']:
            premium_no_base_cases.append(params)

    # Output Analysis Results
    print("\n" + "=" * 30)
    print("ANALYSIS RESULTS")
    print("=" * 30)
    print(f"1. Total cases with Full Access (all 4 sections): {full_access_count}")

    print(f"2. Cases with Premium access but NO Base access: {len(premium_no_base_cases)}")
    if premium_no_base_cases:
        print("   Parameters for these cases (Emp, Ver, Prem, Adm, Ban):")
        for case in premium_no_base_cases:
            # Formatting tuple to 0/1 for consistency
            formatted_case = tuple(int(x) for x in case)
            print(f"   -> {formatted_case}")
        print("\n   Explanation: This occurs when the user is NOT an employee (is_employee=0)")
        print("   but has a premium subscription (is_premium=1), is verified, and not banned.")


if __name__ == "__main__":
    main()