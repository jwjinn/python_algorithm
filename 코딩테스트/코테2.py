from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections.abc import Iterable


# {{ -- Use following Layer & Model classes without modification
class Layer:

    def __init__(self, id: int) -> None:
        """Create Layer with unique id."""
        assert id > 0
        self.id = id
        self.input_layers: set[Layer] = set()
        self.output_layers: set[Layer] = set()

    def __call__(self, *input_layers: Layer) -> Layer:
        """Connect this layer with previous layers."""
        for input_layer in input_layers:
            self.input_layers.add(input_layer)

        for input_layer in input_layers:
            input_layer.output_layers.add(self)

        return self


class Model(ABC):

    @abstractmethod
    def build(self) -> None:
        """Define layers in ther model."""
        raise NotImplementedError

    @abstractmethod
    def layers(self) -> Iterable[Layer]:
        """Connect layers and return all layers included.
        
        The connections between layers should be same between successive calls.
        """
        raise NotImplementedError
# -- }}


class SampleNeuralNetworkModel(Model):

    def build(self) -> None:
        self.x = Layer(1)
        self.y = Layer(2)
        self.z = Layer(3)
        self.out = Layer(4)

        # print(self.x)
        # print(self.y)

    def layers(self) -> Iterable[Layer]:
        # print("layers 선언")
        x = self.x()
        y = self.y(x)
        z = self.z(y)

        # print(x)

        out = self.out(y, z)
        return x, y, z, out


def execution_plan(model: Model) -> list[int]:
    # TODO: implement this
    
    x, y, z, out = Model.layers(Model)

    print(x.id)




    # print(Model.layers(t).x)

    return [x.id, y.id, z.id, out.id]


model = SampleNeuralNetworkModel()
model.build() # x,y,z에 다 들어옴


plan = execution_plan(model)

t = model.layers()

# print("t")
# print(t)
print(plan)  # the answer is [1, 2, 3, 4]