"""
Sprint Coverage Calculator - CLI Version
=========================================
Run from the terminal:

    python sprint_cli.py

The script will prompt you for all required inputs, validate them,
and print a formatted sprint coverage summary.
"""

from calculator import run_calculation

DISCLAIMER = (
    "\nNote: This calculator is a planning aid. "
    "Story points are relative estimates and should support discussion, "
    "not replace team judgment."
)


# ---------------------------------------------------------------------------
# Input helpers
# ---------------------------------------------------------------------------

def prompt_int(prompt: str, min_value: int = 1) -> int:
    """
    Ask the user for a whole number that is >= min_value.
    Keeps asking until valid input is provided.

    Args:
        prompt: The question to display to the user.
        min_value: The smallest acceptable value (default 1).

    Returns:
        A validated integer.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value < min_value:
                print(f"  ✗ Value must be at least {min_value}. Please try again.")
                continue
            return value
        except ValueError:
            print("  ✗ Please enter a whole number (e.g. 5).")


def prompt_float(prompt: str, min_value: float = 0.0,
                 max_value: float = None) -> float:
    """
    Ask the user for a decimal number within an optional range.
    Keeps asking until valid input is provided.

    Args:
        prompt: The question to display to the user.
        min_value: Smallest acceptable value (default 0).
        max_value: Largest acceptable value (None means no upper limit).

    Returns:
        A validated float.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value < min_value:
                print(f"  ✗ Value must be at least {min_value}. Please try again.")
                continue
            if max_value is not None and value > max_value:
                print(f"  ✗ Value must be at most {max_value}. Please try again.")
                continue
            return value
        except ValueError:
            print("  ✗ Please enter a number (e.g. 6.5).")


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def print_separator(char: str = "-", width: int = 40) -> None:
    """Print a horizontal separator line."""
    print(char * width)


def print_summary(results: dict) -> None:
    """
    Print a formatted sprint coverage summary to the terminal.

    Args:
        results: The dict returned by calculator.run_calculation().
    """
    print()
    print("Sprint Coverage Summary")
    print_separator()
    print(f"Team Capacity (hours)         : {results['team_capacity_hours']:.1f} h")
    print(f"Capacity After Buffer (hours) : {results['capacity_after_buffer_hours']:.1f} h")
    print(f"Capacity in Story Points      : {results['capacity_story_points']:.1f} SP")
    print(f"Planned Sprint Scope          : {results['planned_story_points']:.1f} SP")
    print(f"Coverage                      : {results['coverage_percent']:.1f}%")
    print_separator()
    print(f"Status  : {results['status']}")
    print(f"Detail  : {results['message']}")
    print_separator()

    remaining = results["remaining_capacity_sp"]
    if remaining >= 0:
        print(f"Remaining Capacity  : {remaining:.1f} SP  (free capacity)")
    else:
        print(f"Overload Amount     : {abs(remaining):.1f} SP  (scope exceeds capacity)")

    print_separator()
    print(DISCLAIMER)
    print()


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def collect_inputs() -> dict:
    """
    Interactively collect all sprint inputs from the user.

    Returns:
        A dict with all validated input values.
    """
    print()
    print("=" * 40)
    print("   Sprint Coverage Calculator")
    print("=" * 40)
    print("Please enter the sprint details below.")
    print()

    sprint_length_days = prompt_int(
        "Sprint length (days, e.g. 10 for a 2-week sprint): "
    )
    working_days = prompt_int(
        f"Working days in the sprint (≤ {sprint_length_days}): ",
        min_value=1,
    )
    # Sanity-check: working days should not exceed sprint length
    while working_days > sprint_length_days:
        print(
            f"  ✗ Working days ({working_days}) cannot exceed "
            f"sprint length ({sprint_length_days}). Please try again."
        )
        working_days = prompt_int(
            f"Working days in the sprint (≤ {sprint_length_days}): ",
            min_value=1,
        )

    team_members = prompt_int("Number of team members: ")

    productive_hours = prompt_float(
        "Productive hours per person per day (e.g. 6): ",
        min_value=0.5,
        max_value=24.0,
    )

    availability = prompt_float(
        "Team availability percentage (e.g. 80 for 80%): ",
        min_value=1.0,
        max_value=100.0,
    )

    buffer = prompt_float(
        "Buffer percentage for unexpected work (e.g. 15 for 15%): ",
        min_value=0.0,
        max_value=99.0,
    )

    planned_sp = prompt_float(
        "Planned sprint scope in Story Points: ",
        min_value=1.0,
    )

    return {
        "team_members": team_members,
        "working_days": working_days,
        "productive_hours_per_day": productive_hours,
        "availability_percent": availability,
        "buffer_percent": buffer,
        "planned_story_points": planned_sp,
    }


def main() -> None:
    """Main function: collect inputs, run calculation, print summary."""
    try:
        inputs = collect_inputs()
        results = run_calculation(**inputs)
        print_summary(results)
    except KeyboardInterrupt:
        print("\n\nCancelled by user. Goodbye!")


if __name__ == "__main__":
    main()
