# Mô-đun mod: pyswarms.utils.plotters thực hiện các khả năng trực quan hóa khác nhau để tương 
# tác với bầy đàn của bạn. Tại đây, bạn có thể vẽ sơ đồ lịch sử chi phí và tạo hình ảnh động cho 
# bầy đàn của bạn trong cả không gian 2D hoặc 3D.


"""
The mod:`pyswarms.utils.plotters` module implements various
visualization capabilities to interact with your swarm. Here,
ou can plot cost history and animate your swarm in both 2D or
3D spaces.
"""

from .plotters import plot_cost_history, plot_contour, plot_surface

__all__ = ["plotters", "formatters"]
