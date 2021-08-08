from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.faker import Faker


def







def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        bar_datazoom_slider(),
        line_markpoint(),
        pie_rosetype(),
        grid_mutil_yaxis(),
        liquid_data_precision(),
        table_base(),
    )
    page.render("page_draggable_layout.html")


if __name__ == "__main__":
    page_draggable_layout()