# Task 2: System Access Analysis

## 1. Logic Implementation
The logic was modeled using standard boolean algebra based on the provided requirements. A key observation is that `is_verified` and `not is_banned` are prerequisites for **all** access levels. If a user is not verified or is banned, all outputs are strictly `False`.

The logic breakdown:
* **Base:** Requires the user to be an internal `employee`.
* **Premium:** Requires the user to be an `employee` OR have a `premium` subscription.
* **Admin:** Requires the user to be an `admin`.
* **Secret:** Requires the user to be an `admin` OR (`employee` AND `premium`).

## 2. Statistical Analysis
Based on the Truth Table generated for all 32 combinations ($2^5$):

### A. Full Access Analysis
**Question:** In how many cases does the user have full access (to all 4 sections simultaneously)?
**Answer:** **2 cases.**

**Explanation:**
To have full access, all boolean conditions must return `True`.
1.  **Base=True** implies `is_employee = True`.
2.  **Admin=True** implies `is_admin = True`.
3.  **Secret=True** is automatically satisfied if `is_admin = True`.
4.  **Premium=True** is automatically satisfied if `is_employee = True`.

Therefore, the user must be both an **Admin** and an **Employee** (and Verified/Not Banned). The state of `is_premium` does not change the outcome because `is_employee` already grants Premium access logic, and `is_admin` covers Secret access.

The 2 winning combinations are:
1.  `Emp=1, Ver=1, Prem=1, Adm=1, Ban=0`
2.  `Emp=1, Ver=1, Prem=0, Adm=1, Ban=0`

### B. Premium without Base Analysis
**Question:** Is there a combination where the user has access to **Premium**, but **does not** have access to **Base**?
**Answer:** **Yes, there are 2 such cases.**

**Identified Combinations (Emp, Ver, Prem, Adm, Ban):**
1.  `0, 1, 1, 0, 0` (External Premium User)
2.  `0, 1, 1, 1, 0` (External Premium Admin)

**Detailed Explanation:**
* **Base Access** strictly requires `is_employee` to be `True`. If `is_employee` is `False`, Base access is denied regardless of other flags.
* **Premium Access** relies on an **OR** condition: `(is_employee OR is_premium)`.
* Consequently, if a user is **not an employee** (`0`) but **has a premium subscription** (`1`), the Premium condition evaluates to `True`, while the Base condition evaluates to `False`.

**Real-world Context:**
This represents an **external client** or **customer**. They are not part of the company staff (No Base access to internal portals), but they have paid for a subscription (Access to Premium content).