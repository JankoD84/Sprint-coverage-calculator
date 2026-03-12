"""
Sprint Coverage Calculator - Core Logic
========================================
Shared calculation functions used by both the CLI and Streamlit versions.
All business rules and formulas live here to avoid duplication.
"""

# Assumption: 1 Story Point = 4 hours of work
HOURS_PER_STORY_POINT = 4


def calculate_team_capacity(team_members: int,
                            working_days: int,
                            productive_hours_per_day: float,
                            availability_percent: float) -> float:
    """
    Calculate total team capacity in hours.

    Formula:
        team_capacity = team_members × working_days
                        × productive_hours_per_day × (availability / 100)

    Args:
        team_members: Number of people on the team.
        working_days: Number of working days in the sprint.
        productive_hours_per_day: Average focused/productive hours per person per day.
        availability_percent: Team availability as a percentage (e.g. 80 for 80%).

    Returns:
        Total team capacity in hours (float).
    """
    availability_decimal = availability_percent / 100
    return team_members * working_days * productive_hours_per_day * availability_decimal


def calculate_capacity_after_buffer(team_capacity_hours: float,
                                    buffer_percent: float) -> float:
    """
    Reduce team capacity by a buffer to account for unexpected work,
    meetings, interruptions, etc.

    Formula:
        recommended_capacity = team_capacity × (1 - buffer / 100)

    Args:
        team_capacity_hours: Total team capacity in hours.
        buffer_percent: Buffer as a percentage (e.g. 15 for 15%).

    Returns:
        Recommended capacity in hours after the buffer is applied (float).
    """
    buffer_decimal = buffer_percent / 100
    return team_capacity_hours * (1 - buffer_decimal)


def calculate_capacity_in_story_points(capacity_hours: float) -> float:
    """
    Convert hours of capacity into Story Points.

    Formula:
        capacity_sp = capacity_hours / HOURS_PER_STORY_POINT

    Args:
        capacity_hours: Available hours of capacity.

    Returns:
        Capacity expressed in Story Points (float).
    """
    return capacity_hours / HOURS_PER_STORY_POINT


def calculate_coverage_percent(planned_story_points: float,
                                capacity_story_points: float) -> float:
    """
    Calculate how much of the team's capacity is covered by the planned scope.

    Formula:
        coverage = (planned_sp / capacity_sp) × 100

    Args:
        planned_story_points: Story Points in the planned sprint scope.
        capacity_story_points: Story Points the team can realistically deliver.

    Returns:
        Coverage as a percentage (float).  Values above 100 mean overloaded.
    """
    if capacity_story_points == 0:
        # Avoid division by zero; treat as fully overloaded
        return float("inf")
    return (planned_story_points / capacity_story_points) * 100


def determine_sprint_status(coverage_percent: float) -> dict:
    """
    Map a coverage percentage to a human-readable sprint status.

    Status rules:
        < 80%   → Underloaded Sprint
        80–100% → Healthy Sprint Load
        > 100%  → Overloaded Sprint

    Args:
        coverage_percent: The sprint coverage as a percentage.

    Returns:
        A dict with keys "status" and "message".
    """
    if coverage_percent < 80:
        return {
            "status": "Underloaded Sprint",
            "message": "The sprint has extra free capacity.",
        }
    elif coverage_percent <= 100:
        return {
            "status": "Healthy Sprint Load",
            "message": "The sprint scope is realistic and within capacity.",
        }
    else:
        return {
            "status": "Overloaded Sprint",
            "message": "The planned scope exceeds realistic sprint capacity.",
        }


def run_calculation(team_members: int,
                    working_days: int,
                    productive_hours_per_day: float,
                    availability_percent: float,
                    buffer_percent: float,
                    planned_story_points: float) -> dict:
    """
    Run the full sprint coverage calculation and return all results.

    This is the single entry-point used by both the CLI and Streamlit frontends.

    Args:
        team_members: Number of team members.
        working_days: Working days in the sprint.
        productive_hours_per_day: Productive hours per person per day.
        availability_percent: Team availability (0–100).
        buffer_percent: Buffer for unexpected work (0–100).
        planned_story_points: Story Points in the planned sprint scope.

    Returns:
        A dict containing all intermediate values and final results.
    """
    team_capacity_hours = calculate_team_capacity(
        team_members, working_days, productive_hours_per_day, availability_percent
    )

    capacity_after_buffer_hours = calculate_capacity_after_buffer(
        team_capacity_hours, buffer_percent
    )

    capacity_story_points = calculate_capacity_in_story_points(
        capacity_after_buffer_hours
    )

    coverage_percent = calculate_coverage_percent(
        planned_story_points, capacity_story_points
    )

    sprint_status = determine_sprint_status(coverage_percent)

    # Remaining capacity: positive means free capacity, negative means overload
    remaining_capacity_sp = capacity_story_points - planned_story_points

    return {
        "team_capacity_hours": round(team_capacity_hours, 2),
        "capacity_after_buffer_hours": round(capacity_after_buffer_hours, 2),
        "capacity_story_points": round(capacity_story_points, 2),
        "planned_story_points": planned_story_points,
        "coverage_percent": round(coverage_percent, 1),
        "remaining_capacity_sp": round(remaining_capacity_sp, 2),
        "status": sprint_status["status"],
        "message": sprint_status["message"],
    }
