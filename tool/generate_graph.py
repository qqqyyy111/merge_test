import pyecharts.options as opts
from pyecharts.charts import Line

from tool.loadData import load_json_mt
from tool.seconds2time import seconds_to_time


def get_data():
    load_json_mt(mt_json)


def generate_fps_graph():
    pass


def generate_cpu_graph():
    pass


def generate_memory_graph():
    pass


def generate_gpu_graph():
    pass



def generate_perf_graph(name, x_data, y_data):
    (
        Line()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="FPS"),
            tooltip_opts=opts.TooltipOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(

            series_name=name,
            y_axis=y_data,
            symbol="emptyCircle",
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
            .render("Perf.html")
    )


if __name__ == '__main__':
    mt_json = '/Users/qiuyu/Desktop/test_PerfMapMRN_Andr_PnP_polyline_MT.json'
    # tx_json = '/Users/qiuyu/Desktop/test_PerfMapMRN_Andr_PnP_polyline_TX.json'

    x_data_mt, y_data_mt = load_json_mt(mt_json)
    x_data_mt = seconds_to_time(x_data_mt)

    # generate_perf_graph('美团', x_data_mt, y_data_mt)
