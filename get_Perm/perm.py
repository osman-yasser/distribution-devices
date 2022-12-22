# perm.py
"""
    This module has one class permute, used to instantiate an object,
    which takes to parameters in instantiate process:
        iterable: a list contains points.
        r: an int contains the number of devices.
"""

from itertools import permutations
import math
from typing import Iterable
from random import choice, randrange

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')


class permute():
    """Generate permutation object hold all permutations"""

    def __init__(self, iterable: Iterable, r: int) -> None:
        """instantiate permute object"""
        self.__permutation = None
        self.__dict = None
        self.__iterable = iterable
        self.__iterable_len = len(iterable)
        self.__r = r
        


    # Properties
    @property
    def size(self) -> int:
        """size property for the number of permutations"""
        return self.__len__()

    @property
    def iterable(self) -> Iterable:
        """iterable property for return the iterable was been passed"""
        return self.__iterable

    @property
    def r(self) -> int:
        """r property for return the number of devices was been passed"""
        return self.__r

    @property
    def counts_device_in_every_points(self) -> dict:
        """
            for return a dictionary:
                Key: represent device notation
                Value: ndarry represet how many this device appear in point(point is the index of value+1)
        """
        self.__get_count_of_points()
        return self.__dict

    @property
    def bar_plot(self) -> None:
        """for plot how many this device appear in a point as a bar plot"""
        self.__private_bar_plot()
        plt.legend()
        plt.tight_layout()
        plt.show()


    # Public methods
    def random_sampling(self, test_cases: int) -> np.ndarray:
        """
            generate unique permutations in numpy array using random sampling.
            using Fisher-Yates algorithm to generate permutations.
        """
        n_set = set()
        while len(n_set) < test_cases:
            temp = self.__shuffle(self.__iterable.copy(), self.__r)
            n_set.add(temp)
        n_list = list(n_set)
        np_arry = np.array(n_list, 'int')
        return np_arry


    # Private methods
    def __get_count_of_points(self) -> None:
        """
            to get how many this device appear in points,
            and generate self.__dict attribute
        """
        if self.__permutation == None:
            self.__permutation = permutations(self.__iterable, self.__r)
        arry = np.array([i for i in self], 'int')
        self.__dict = dict()
        for i in range(self.__r):
            uni, counts = np.unique(arry[0: self.__len__(), i], return_counts=True)
            self.__dict[chr(i + 65)] = counts

    def __private_bar_plot(self) -> None:
        """
            to plot as a bar plot
        """
        if self.__dict == None:
            self.__get_count_of_points()
        
        # set width of bar
        barWidth = 0.25
        fig = plt.subplots(figsize =(12, 8))

        # Set position of bar on X axis
        br_temp = np.arange(self.__iterable_len)
        br = list()
        for _ in range(0, self.__r):
            br.append(br_temp)
            br_temp = br_temp + barWidth

        # Make the plot
        for i in range(self.__r):
            plt.bar(br[i], self.__dict[chr(i + 65)], width=barWidth, edgecolor ='grey', label= chr(i + 65))

        # Adding Xticks
        plt.xlabel('Points', fontweight ='bold', fontsize = 15)
        plt.ylabel('Counts', fontweight ='bold', fontsize = 15)
        plt.xticks([r + barWidth for r in range(self.__iterable_len)],[f'Point {i}' for i in range(1, self.__iterable_len+1)])

    def __shuffle(self, n: list, r: int) -> tuple:
        """
            choice random points equal to the number of devices
            and shuffle this list
        """
        perm = list()
        for i in range(r):
            perm.append(choice(n))
            n.remove(perm[i])
        for i in range(r-1, 0, -1):
            j = randrange(0, i+1)
            perm[i], perm[j] = perm[j], perm[i]
        return tuple(perm)


    # Dunder methods
    def __len__(self) -> int:
        """get the number of permutations"""
        return int(math.factorial(self.__iterable_len) / math.factorial(self.__iterable_len - self.__r))

    def __iter__(self):
        """make the object a iterable object"""
        if self.__permutation == None:
            self.__permutation = permutations(self.__iterable, self.__r)
        return self.__permutation.__iter__()

