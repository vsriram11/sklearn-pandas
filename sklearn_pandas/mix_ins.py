from typing import Union

import databricks.koalas as ks
import pandas as pd


class DataframeMixin:
    """Mixin class for all transformers in scikit-learn."""

    def _set_df_library(self, X: Union[pd.DataFrame, ks.DataFrame]):
        """ Detect X and set .dflib_ to pd or ks or pyspark.

        """
        if isinstance(X, pd.DataFrame):
            self.dflib_ = pd
        elif isinstance(X, ks.DataFrame):
            self.dflib_ = ks
        else:
            raise ValueError("Only pandas and koalas dataframe are supported.")