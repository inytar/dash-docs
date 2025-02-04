import dash_html_components as html
import dash_table
from tutorial.utils.convert_props_to_list import generate_prop_info


layout = html.Div([
    html.H1('Dash Interactive Table Reference'),
    generate_prop_info('DataTable', dash_table)
])
