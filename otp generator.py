{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled7.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMuATAtaSe7aTKpQsSwu3Gc",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/shreenivasreddy/Garbage-Monitoring-using-IOT/blob/master/otp%20generator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_4VWsyx8N-AR",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import random"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uQPQp5yrOCSR",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "261a2210-07eb-4d80-ec01-f647a258ef18"
      },
      "source": [
        "otp = random.randrange(10000, 100000)\n",
        "print(otp)"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "74767\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LvOBWHPKOJKy",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "d7b6a4f3-184e-4a8c-da16-a0a15568f43c"
      },
      "source": [
        "user = int(input('Enter the otp: '))\n",
        "if otp == user:\n",
        "  print('Access granted!!!')\n",
        "else:\n",
        "  print('Access Denied!!1')"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter the otp: 74767\n",
            "Access granted!!!\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OTlM0xNpOVYs",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}