import plotly.graph_objs as go
from utilz.mock_sleep_data import get_mock_sleep_data

def plot_sleep_duration_chart():
    current_data, projected_data = get_mock_sleep_data()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    extended_days = days + [f"Next {day}" for day in days]

    current_values = list(current_data.values())
    projected_values = list(projected_data.values())

    current_values_extended = current_values + projected_values
    projected_values_extended = projected_values + projected_values

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=extended_days, 
        y=current_values_extended, 
        mode='lines+markers',
        name='Current Sleep',
        line=dict(color='blue'),
        marker=dict(size=10)
    ))

    fig.add_trace(go.Scatter(
        x=extended_days, 
        y=projected_values_extended, 
        mode='lines+markers',
        name='Projected Sleep',
        line=dict(color='green', dash='dash'),
        marker=dict(size=10)
    ))

    fig.update_layout(
        title="Current vs Projected Sleep Quality Over Two Weeks",
        xaxis_title="Days",
        yaxis_title="Hours of Sleep",
        xaxis=dict(tickmode='array', tickvals=list(range(len(extended_days))), ticktext=extended_days),
        hovermode='x unified'
    )

    return fig