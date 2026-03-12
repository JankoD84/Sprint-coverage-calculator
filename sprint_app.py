"""
Sprint Coverage Calculator - Streamlit Web App
================================================
Run with:

    streamlit run sprint_app.py

Provides a clean, interactive UI for calculating sprint coverage,
with sliders, a calculate button, and a colour-coded status display.
"""

import streamlit as st
from calculator import run_calculation

DISCLAIMER = (
    "**Note:** This calculator is a planning aid. "
    "Story points are relative estimates and should support discussion, "
    "not replace team judgment."
)

# Map each status to a Streamlit colour keyword used in st.success / st.warning / st.error
STATUS_STYLE = {
    "Underloaded Sprint": "warning",
    "Healthy Sprint Load": "success",
    "Overloaded Sprint": "error",
}

# Emoji decoration for each status
STATUS_EMOJI = {
    "Underloaded Sprint": "💤",
    "Healthy Sprint Load": "✅",
    "Overloaded Sprint": "🔥",
}


def render_status_box(results: dict) -> None:
    """
    Display the sprint status using a colour-coded Streamlit callout.

    Args:
        results: The dict returned by calculator.run_calculation().
    """
    status = results["status"]
    emoji = STATUS_EMOJI.get(status, "")
    message = results["message"]
    coverage = results["coverage_percent"]
    style = STATUS_STYLE.get(status, "info")

    text = f"{emoji} **{status}** — Coverage: **{coverage:.1f}%**  \n{message}"

    if style == "success":
        st.success(text)
    elif style == "warning":
        st.warning(text)
    elif style == "error":
        st.error(text)
    else:
        st.info(text)


def render_metrics(results: dict) -> None:
    """
    Display the key numbers as Streamlit metric tiles.

    Args:
        results: The dict returned by calculator.run_calculation().
    """
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Team Capacity",
            value=f"{results['team_capacity_hours']:.1f} h",
        )
        st.metric(
            label="Capacity After Buffer",
            value=f"{results['capacity_after_buffer_hours']:.1f} h",
        )

    with col2:
        st.metric(
            label="Capacity in Story Points",
            value=f"{results['capacity_story_points']:.1f} SP",
        )
        st.metric(
            label="Planned Sprint Scope",
            value=f"{results['planned_story_points']:.1f} SP",
        )

    with col3:
        remaining = results["remaining_capacity_sp"]
        if remaining >= 0:
            st.metric(
                label="Remaining Capacity",
                value=f"{remaining:.1f} SP",
                delta=f"+{remaining:.1f} SP free",
                delta_color="normal",
            )
        else:
            st.metric(
                label="Overload Amount",
                value=f"{abs(remaining):.1f} SP",
                delta=f"-{abs(remaining):.1f} SP over capacity",
                delta_color="inverse",
            )

        st.metric(
            label="Sprint Coverage",
            value=f"{results['coverage_percent']:.1f}%",
        )


def render_coverage_bar(coverage_percent: float) -> None:
    """
    Draw a visual coverage bar using a Streamlit progress element.
    Capped at 100% visually, but the true value is shown in text.

    Args:
        coverage_percent: The sprint coverage as a percentage.
    """
    st.subheader("Coverage Visual")

    # st.progress accepts a value between 0.0 and 1.0
    bar_value = min(coverage_percent / 100, 1.0)
    st.progress(bar_value)

    if coverage_percent > 100:
        st.caption(
            f"⚠️ Bar is capped at 100%. Actual coverage is **{coverage_percent:.1f}%** "
            "(sprint is overloaded)."
        )
    else:
        st.caption(f"Sprint is {coverage_percent:.1f}% loaded.")


def main() -> None:
    """Build and render the full Streamlit application."""

    # -----------------------------------------------------------------------
    # Page configuration
    # -----------------------------------------------------------------------
    st.set_page_config(
        page_title="Sprint Coverage Calculator",
        page_icon="📊",
        layout="centered",
    )

    # -----------------------------------------------------------------------
    # Header
    # -----------------------------------------------------------------------
    st.title("📊 Sprint Coverage Calculator")
    st.markdown(
        "Compare your **team capacity** against your **planned sprint scope** "
        "and find out whether the sprint is realistically achievable."
    )
    st.divider()

    # -----------------------------------------------------------------------
    # Input section
    # -----------------------------------------------------------------------
    st.subheader("Sprint & Team Settings")

    col_left, col_right = st.columns(2)

    with col_left:
        sprint_length = st.number_input(
            "Sprint length (days)",
            min_value=1,
            max_value=90,
            value=10,
            step=1,
            help="Total calendar length of the sprint (e.g. 10 for a 2-week sprint).",
        )

        working_days = st.number_input(
            "Working days in sprint",
            min_value=1,
            max_value=int(sprint_length),
            value=min(10, int(sprint_length)),
            step=1,
            help="Actual days the team will work (excluding holidays, etc.).",
        )

        team_members = st.number_input(
            "Number of team members",
            min_value=1,
            max_value=100,
            value=5,
            step=1,
            help="Developers, testers, designers — everyone contributing Story Points.",
        )

        productive_hours = st.slider(
            "Productive hours per person per day",
            min_value=1.0,
            max_value=10.0,
            value=6.0,
            step=0.5,
            help=(
                "Focused coding/design hours. Excludes stand-ups, "
                "admin, and context switching."
            ),
        )

    with col_right:
        availability = st.slider(
            "Team availability (%)",
            min_value=10,
            max_value=100,
            value=80,
            step=5,
            help=(
                "Overall availability considering leave, part-time members, "
                "and other commitments."
            ),
        )

        buffer = st.slider(
            "Buffer for unexpected work (%)",
            min_value=0,
            max_value=50,
            value=15,
            step=5,
            help=(
                "Reserve capacity for bug fixes, incidents, scope-creep, "
                "and other surprises."
            ),
        )

        planned_sp = st.number_input(
            "Planned sprint scope (Story Points)",
            min_value=1,
            max_value=5000,
            value=40,
            step=1,
            help="Total Story Points of all tickets planned for this sprint.",
        )

    st.divider()

    # -----------------------------------------------------------------------
    # Validation warning
    # -----------------------------------------------------------------------
    if working_days > sprint_length:
        st.warning(
            f"Working days ({working_days}) exceeds sprint length ({sprint_length}). "
            "Please adjust your inputs."
        )
        return

    # -----------------------------------------------------------------------
    # Calculate button
    # -----------------------------------------------------------------------
    if st.button("Calculate Sprint Coverage", type="primary", use_container_width=True):
        results = run_calculation(
            team_members=team_members,
            working_days=int(working_days),
            productive_hours_per_day=productive_hours,
            availability_percent=availability,
            buffer_percent=buffer,
            planned_story_points=planned_sp,
        )

        st.divider()
        st.subheader("Sprint Coverage Summary")

        # Status callout (colour-coded)
        render_status_box(results)

        st.markdown("")  # small spacer

        # Metric tiles
        render_metrics(results)

        st.markdown("")  # small spacer

        # Visual progress bar
        render_coverage_bar(results["coverage_percent"])

        st.divider()

        # Assumption note
        st.caption("Assumption: 1 Story Point = 4 hours of work.")

        # Disclaimer
        st.info(DISCLAIMER)

    else:
        # Show a friendly prompt when the app first loads
        st.markdown(
            "> Fill in the sprint settings above and click **Calculate Sprint Coverage**."
        )


if __name__ == "__main__":
    main()
