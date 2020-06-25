# Copyright 2020 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Oryx is a neural network mini-library built on top of Jax."""
from oryx import bijectors
from oryx import core
from oryx import distributions
from oryx import experimental
from oryx import util
from oryx.core.pytree import Pytree
from oryx.core.serialize import deserialize
from oryx.core.serialize import serialize
from oryx.core.state.api import init
from oryx.core.state.api import Shape
from oryx.core.state.api import spec
from oryx.core.state.module import assign
from oryx.core.state.module import Module
from oryx.core.state.module import variable
