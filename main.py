import plotly.express as px
df = px.data.gapminder()
df1 = df.loc[df['country'].isin(['India', 'Sri Lanka', 'Pakistan'])]



# %%
px.scatter(df1, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="country", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

# %%
fig = px.line(
    df1,
    x="gdpPercap",
    y="lifeExp",
    line_group="country",
    color="country",
    hover_name="country",
    log_x=True,
    range_x=[100, 100000],
    range_y=[25, 90]
)
fig.update_traces(mode="lines+markers")  # Show both lines and markers
fig.update_layout(transition={'duration': 500})  # Smoother animation
fig.show()

