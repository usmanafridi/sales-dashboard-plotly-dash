from itertools import filterfalse
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import numpy as np



def bar_chart(x, y,yaxis, text, orientation):
	fig = {
		"data": [

			go.Bar(
				x = x,
				y = y,
				orientation=f'{orientation}',
				
			
				marker=dict(color='rgb(179,226,205)'),
				# mode = "lines",
				# line = {
				# 	"width": 3,
				# 	"color": "#ff00ff"
				# },
				hoverinfo = "text",
				hovertemplate = "<b>Month</b>: %{x} <br>Value<b></b>: %{y:,.0f}<extra></extra>",
				

			),

				go.Scatter(
				x = x,
				y = y,
				
				
			
			
				mode = "lines",
				line = {
					"width": 2,
					"color": "orange"
				},
				hoverinfo = "text",
				hovertemplate = "<b>Month</b>: %{x} <br>Value<b></b>: %{y:,.0f}<extra></extra>",
				

			)
		],
		"layout": go.Layout(
			title = {
				"text": f" {text}    ",
				"y": 0.93,
				"x": 0.5,
				"xanchor": "center",
				"yanchor": "top"
			},
			titlefont = {
				"color": "black",
				"size": 30
			},
			xaxis = {
				
				"color": "black",
				"showline": True,
				"showgrid": True,
				"showticklabels": True,
				"tickangle":0,
				"linecolor": "white",
				"linewidth": 1,
				"ticks": "outside",
				"tickfont": {
					"family": "Aerial",
					"color": "black",
					"size": 20
				}
			},
			yaxis = {
				"title": f"<b>{yaxis}</b>",
				"color": "black",
				"showline": True,
				"showgrid": True,
				"showticklabels": True,
				"linecolor": "white",
				"linewidth": 1,
				"ticks": "outside",
				"tickfont": {
					"family": "Aerial",
					"color": "black",
					"size": 20
				}
			},
			font = {
				"family": "sans-serif",
				"color": "black",
				"size": 20
			},
			hovermode = "closest",
			# textposition='outside',
			paper_bgcolor = " #f2f2f2",
			plot_bgcolor = " #f2f2f2",
			showlegend=False,
		)
	}
	# Return the figure
	# fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

	
	return fig


def bar_chart_cat(x, y,yaxis, text, orientation):
	fig = {
		"data": [

			go.Bar(
				x = x,
				y = y,
				orientation=f'{orientation}',
				
			
				marker=dict(color='rgb(179,226,205)'),
				# mode = "lines",
				# line = {
				# 	"width": 3,
				# 	"color": "#ff00ff"
				# },
				hoverinfo = "text",
				hovertemplate = "<b>Month</b>: %{x} <br>Value<b></b>: %{y:,.0f}<extra></extra>",
				

			)
		],
		"layout": go.Layout(
			title = {
				"text": f" {text}    ",
				"y": 0.93,
				"x": 0.5,
				"xanchor": "center",
				"yanchor": "top"
			},
			titlefont = {
				"color": "black",
				"size": 30
			},
			margin ={
				'l':70, 
				'r':30, 
				't':80,
				'b':200},
			xaxis = {
				
				"color": "black",
				"showline": True,
				"showgrid": True,
				"showticklabels": True,
				"tickangle":70,
				"linecolor": "white",
				"linewidth": 1,
				"ticks": "outside",
				"tickfont": {
					"family": "Aerial",
					"color": "black",
					"size": 13
				}
			},
			yaxis = {
				"title": f"<b>{yaxis}</b>",
				"color": "black",
				"showline": True,
				"showgrid": True,
				"showticklabels": True,
				"linecolor": "white",
				"linewidth": 1,
				"ticks": "outside",
				"tickfont": {
					"family": "Aerial",
					"color": "black",
					"size": 15
				}
			},
			font = {
				"family": "sans-serif",
				"color": "black",
				"size": 20
			},
			hovermode = "closest",
			# textposition='outside',
			paper_bgcolor = " #f2f2f2",
			plot_bgcolor = " #f2f2f2",
			legend = {
				"orientation": "h",
				"bgcolor": "#1f2c56",
				"xanchor": "center",
				"x": 0.5,
				"y": -0.7
			}
		)
	}
	# Return the figure
	# fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')


	return fig ## Can be also used instead of Pie Chart.


def pie_chart(labels, values, title):



	colors = ['rgb(179,226,205)', 'rgb(253,205,172)', 'rgb(203,213,232)', 'rgb(244,202,228)', 'rgb(230,245,201)', 'rgb(255,242,174)', 'rgb(241,226,204)', 'rgb(204,204,204)']
	# Build the figure


	fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent')])

	fig.update_traces(hoverinfo = "label+value+percent", hole = 0.3,
	rotation = 0, marker=dict(colors=colors))

	fig.update_layout(
	paper_bgcolor = " #f2f2f2",
	plot_bgcolor = " #f2f2f2",
	font=dict(family='sans-serif',
                      color='black',
                      size=20),


	)

	
	fig.update_traces(textposition='inside'),
	
	fig.update_layout(
            
            margin={'l': 10, 'b': 45, 't': 45, 'r': 10},
            legend=dict(font=dict(size=15)),),
			
	fig.update_layout(title_text=f"{title}", title_x=0.5),


	fig.update_layout(
	autosize=True,

	height=400,)

	# fig.update_layout(legend=dict(yanchor="bottom",  y=1.02, xanchor="left", x=0.2), legend_orientation="h"),
	fig.update_layout(showlegend=False)





	# fig = px.pie(dff, names='CustomerID',values='Total',  title='Top 10 most customers')
	return fig




###### FOR COMPANY STUDIO 224

df= pd.read_csv("Transactions.csv")
# df['Expense By Category'] = np.abs(df['Expense By Category'])
df['Date'] = pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.month_name()
# year = [2019, 2020, 2021, 2022]
# companies= df["Store"].unique()

df_company= df[df["Store"]== "Store A"]



# year = df_company['Date'].dt.year.unique().tolist()


## Cards Values ##

unique_categories= df_company.Sales_Category.nunique()
df_revenue= df_company.groupby(["Month", "Month_Name"])["Transaction_Amount"].agg(lambda x: x[x>0].sum()).reset_index()

revenue= round(df_revenue.Transaction_Amount.sum(),2)

df_expense= df_company.groupby(["Month", "Month_Name"])["Transaction_Amount"].agg(lambda x: x[x<0].sum()).reset_index()

expense= round(abs(df_expense.Transaction_Amount.sum()),2)

# amount_spend= round(df2.Transaction_Amount.sum(),2)

unique_trans= df_company.Date.nunique()
#######################



#### PIE CHART VALUES #####


df_revenue= df_company.groupby("Sales_Category")["Revenue By Category"].first().reset_index()

df_revenue_sort= df_revenue.sort_values(['Revenue By Category'], ascending=False)
df_revenue_greater_zero= df_revenue_sort[df_revenue_sort["Revenue By Category"] > 0]


df_revenue_20= df_revenue_greater_zero.head()


df_company['Expense By Category'] = np.abs(df_company['Expense By Category'])
df_expense= df_company.groupby("Sales_Category")["Expense By Category"].first().reset_index()
df_expense_sort= df_expense.sort_values(['Expense By Category'], ascending=False)

df_expense_greater_zero= df_expense_sort[df_expense_sort["Expense By Category"] > 0]
df_expense_20= df_expense_greater_zero.head()



figure_expense= pie_chart(df_expense_20["Sales_Category"],df_expense_20["Expense By Category"], "Top Categories by Expense")


figure_revenue= pie_chart(df_revenue_20["Sales_Category"], df_revenue_20["Revenue By Category"], "Top Categories by Revenue")



#### BAR CHART VALUES ####


# df_revenue= df2.groupby(["Month", "Month_Name"])["Revenue By Category"].mean().reset_index()

def filter_df(year):

	df1=df_company.copy()

	df2=df1[df1['Year']== year]
	df_revenue= df2.groupby(["Month", "Month_Name"])["Transaction_Amount"].agg(lambda x: x[x>0].sum()).reset_index()

	df_revenue_sort= df_revenue.sort_values(['Month'], ascending=True)

	df_revenue_20= df_revenue_sort.head(20)

	df_expense= df2.groupby(["Month", "Month_Name"])["Transaction_Amount"].agg(lambda x: x[x<0].sum()).reset_index()
	df_expense['Transaction_Amount'] = np.abs(df_expense['Transaction_Amount'])

	df_expense_sort= df_expense.sort_values(['Month'], ascending=True)

	df_expense_20= df_expense_sort.head(20)

	df_profit = df2.groupby(["Month", "Month_Name"])["Transaction_Amount"].sum().reset_index()
	df_profit_sort= df_profit.sort_values(['Month'], ascending=True)


	figure_expense_month= bar_chart(df_expense_20["Month_Name"], df_expense_20["Transaction_Amount"], "Expense", f"Expense in year {year}", "v")
	figure_revenue_month= bar_chart(df_revenue_20["Month_Name"], df_revenue_20["Transaction_Amount"],"Revenue",f"Revenue in year {year}", "v")
	figure_profit= bar_chart(df_profit_sort["Month_Name"], df_profit_sort["Transaction_Amount"],"Profit", f"Profit in year {year}", "v")

	return figure_expense_month, figure_revenue_month, figure_profit


figure_expense_month_2021=filter_df(2021)[0]
figure_revenue_month_2021= filter_df(2021)[1]

figure_profit_month_2021=filter_df(2021)[2]


figure_expense_month_2022=filter_df(2022)[0]
figure_revenue_month_2022= filter_df(2022)[1]

figure_profit_month_2022=filter_df(2022)[2]






app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
server = app.server

# Build the layout
app.layout = html.Div(
	children = [
		# (First row) Header: Logo - Title - Last updated



			html.Div([
				html.Div([
				html.H2(
							children = "Sales Dashboard for Company ABC",
							style = {
								"textAlign": "center",
								"color": "black",
								
								"fontSize": 30,
								"font-weight": "bold",
							}
						),
				],className="title")
			],className = "row flex-display"),
		# (Second row) Cards
		html.Div(
			children = [
				# (Column 1)
				html.Div(
					children = [
						# Title
						html.H6(
							children = "Total Items Categories",
							style = {
								"textAlign": "center",
								"color": "black"
							}
						),
						# Total value
						html.P(
							id="cat",
							children = unique_categories,
							style = {
								"textAlign": "center",
								"color": "#000099",
								"fontSize": 30,
								"font-weight": "bold",
							}
						),

					],
					className = "card_container card_size"
				),
				
				html.Div(
					children = [
						# Title
						html.H6(
							children = "Revenue",
							style = {
								"textAlign": "center",
								"color": "black"
							}
						),
						# Total value
						html.P(
							id="amount",
							children = "$ "+ str(revenue),
							style = {
								"textAlign": "center",
								"color": "#000099",
								"fontSize": 30,
								"font-weight": "bold",
							}
						),

					],
					className = "card_container card_size_2"
				),
				
				html.Div(
					children = [
						# Title
						html.H6(
							children = "Number of Transactions",
							style = {
								"textAlign": "center",
								"color": "black"
							}
						),
						# Total recovered
						html.P(
							id="transactions",
							children = unique_trans,
							style = {

								"textAlign": "center",
							"color": "#000099",
								"fontSize": 30,
								"font-weight": "bold",
							}
						),

					],
					className = "card_container card_size_3"
				),
				# (Column 4): 
				html.Div(
					children = [
						# Title
						html.H6(
							children = "Expenses",
							style = {
								"textAlign": "center",
								"color": "black"
							}
						),
						# Total v
						html.P(
							id="avg_trans",
							children ="$ "+ str(expense),
							style = {
								"textAlign": "center",
								"color": "#000099",
								"fontSize": 30,
								"font-weight": "bold",

							}
						),

					],
					className = "card_container card_size_2"
				)
			],
			className = "row flex-display"
		),




		#Fourth Row
				html.Div(
			children = [
				

				
				html.Div(
					children = [
				
						# Donut chart
						dcc.Graph(
							figure=figure_expense,
								
							# figure= pie_chart(df_expense_20["Category"], df_expense_20["Expense By Category"], "Expense")
							
						)
					],
					className = "create_container pie_chart",
				
				),
	

			
				
				html.Div(

					children = [

					
						dcc.Graph(
							figure=figure_revenue,
							
						# figure= pie_chart(df_revenue_20["Category"], df_revenue_20["Revenue By Category"], "Revenue")
						)
					],className = "create_container pie_chart_2"
				)
			],
			className = "row flex-display"
		),



		

				html.Div([

					html.Div([
						dcc.Graph(figure=figure_expense_month_2021),
						],className= "create_container bar_div"),

					],className="row flex-display"),


					html.Div([

					html.Div([
						dcc.Graph( figure=figure_revenue_month_2021),
						],className= "create_container bar_div"),

					],className="row flex-display"),

					html.Div([

					html.Div([
						dcc.Graph(figure=figure_profit_month_2021)
						],className= "create_container bar_div"),

					],className="row flex-display"),




					#### 2022 #####


		

				html.Div([

					html.Div([
						dcc.Graph(id="bar_chart_expense", figure=figure_expense_month_2022),
						],className= "create_container bar_div"),

					],className="row flex-display"),


					html.Div([

					html.Div([
						dcc.Graph(id="bar_chart_revenue", figure=figure_revenue_month_2022),
						],className= "create_container bar_div"),

					],className="row flex-display"),

					html.Div([

					html.Div([
						dcc.Graph(figure=figure_profit_month_2022),
						],className= "create_container bar_div"),

					],className="row flex-display"),












	],
	id = "mainContainer",
	style = {
		"display": "flex",
		"flex-direction": "column"
	}
)








# Run the app
if __name__ == "__main__":
  app.run_server(debug = False)
