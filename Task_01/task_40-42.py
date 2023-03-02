{
    "nbformat": 4,
    "nbformat_minor": 0,
    "metadata": {
        "colab": {
            "provenance": []
        },
        "kernelspec": {
            "name": "python3",
            "display_name": "Python 3"
        },
        "language_info": {
            "name": "python"
        }
    },
    "cells": [
        {
            "cell_type": "markdown",
            "source": [
                "# Задача 40: \n",
                "\n",
                "1. Работать с файлом california_housing_train.csv, который находится в папке sample_data.\n",
                "\n",
                "2. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)"
            ],
            "metadata": {
                "id": "xgY8jasH4t6r"
            }
        },
        {
            "cell_type": "code",
            "source": [
                "import pandas as pd"
            ],
            "metadata": {
                "id": "3bYXTFGh4wPQ"
            },
            "execution_count": 1,
            "outputs": []
        },
        {
            "cell_type": "code",
            "source": [
                "df = pd.read_csv('sample_data/california_housing_train.csv')"
            ],
            "metadata": {
                "id": "SwOWMPfS4z0I"
            },
            "execution_count": 2,
            "outputs": []
        },
        {
            "cell_type": "code",
            "source": [
                "df[df['population'] >= 0 & (df['population'] <= 500)]['median_house_value'].mean()"
            ],
            "metadata": {
                "colab": {
                    "base_uri": "https://localhost:8080/"
                },
                "id": "I5_23xv85hKv",
                "outputId": "7ad51818-dd23-4b30-8614-798afffacdf1"
            },
            "execution_count": 3,
            "outputs": [
                {
                    "output_type": "execute_result",
                    "data": {
                        "text/plain": [
                            "207300.91235294117"
                        ]
                    },
                    "metadata": {},
                    "execution_count": 3
                }
            ]
        },
        {
            "cell_type": "markdown",
            "source": [
                "# Задача 42: \n",
                "* Узнать какая максимальная households в зоне минимального значения population"
            ],
            "metadata": {
                "id": "3WLqRP7a-OKy"
            }
        },
        {
            "cell_type": "code",
            "source": [
                "df[df['population'] == df['population'].min()]['households'].max()"
            ],
            "metadata": {
                "colab": {
                    "base_uri": "https://localhost:8080/"
                },
                "id": "TUFKRvpB-T6I",
                "outputId": "4a4a54d5-f532-48ff-aa32-f8cf196a9fe0"
            },
            "execution_count": 8,
            "outputs": [
                {
                    "output_type": "execute_result",
                    "data": {
                        "text/plain": [
                            "4.0"
                        ]
                    },
                    "metadata": {},
                    "execution_count": 8
                }
            ]
        }
    ]
}
