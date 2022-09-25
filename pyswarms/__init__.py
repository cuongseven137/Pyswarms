# -*- coding: utf-8 -*-
# Điều này bao gồm các tiện ích khác nhau để giúp tối ưu hóa. 
# Một số tiện ích bao gồm các chức năng mục tiêu điểm chuẩn, 
# tìm kiếm siêu tham số và các chức năng vẽ biểu đồ.
"""
Particle Swarm Optimization (PSO) toolkit
=========================================
PySwarms is a particle swarm optimization (PSO) toolkit that enables
researchers to test variants of the PSO technique in different contexts.
Users can define their own function, or use one of the benchmark functions
in the library. It is built on top of :code:`numpy` and :code:`scipy`, and
is very extensible to accommodate other PSO variations.
"""

__author__ = """Lester James V. Miranda"""
__email__ = "ljvmiranda@gmail.com"
__version__ = "1.3.0"

from .single import global_best, local_best, general_optimizer
from .discrete import binary
from .utils.decorators import cost

__all__ = ["global_best", "local_best", "general_optimizer", "binary", "cost"]
