import pyecharts.options as opts
from pyecharts.charts import Line

# x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
# y_data = [820, 932, 901, 934, 1290, 1330, 1320]
#
#
# line = Line()
# line.set_global_opts(
#     title_opts=opts.TitleOpts(title="overlay"),
#     tooltip_opts=opts.TooltipOpts(trigger="axis"),
#     xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
#     yaxis_opts=opts.AxisOpts(
#         type_="value",
#         axistick_opts=opts.AxisTickOpts(is_show=True),
#     ),
# )
#
# line.add_xaxis(xaxis_data=x_data)
# line.add_yaxis(
#     series_name="1",
#
# )
#
#
# line.render("html//stacked_line.html")


x_data = ["Mon", "Tue", "Wed", "Thu"]  # "Fri", "Sat", "Sun"]
y_data1 = [820, 932, 901, 934, 1290, 1330, 1320]
# y_data2 = [100, 200, 300, 400, 500, 600, 700]

line = Line()
line.set_global_opts(tooltip_opts=opts.TooltipOpts(is_show=False),
                     xaxis_opts=opts.AxisOpts(type_="category", split_number=4),
                     yaxis_opts=opts.AxisOpts(
                         type_="value",
                         axistick_opts=opts.AxisTickOpts(is_show=True),  # 是否显示坐标轴刻度
                         splitline_opts=opts.SplitLineOpts(is_show=True), ), )  # 是否显示分割线

line.add_xaxis(xaxis_data=x_data)
line.add_yaxis(
    series_name="",
    y_axis=y_data1,
    symbol="emptyCircle",
    is_symbol_show=True,

    label_opts=opts.LabelOpts(is_show=False),
)

# line.add_yaxis(
#         series_name="",
#         y_axis=y_data2,
#         symbol="emptyCircle",
#         is_symbol_show=True,
#         label_opts=opts.LabelOpts(is_show=False),
# )


line.render("html//basic_line_chart2.html")
