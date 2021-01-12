# -*- coding: utf-8 -*-
from matplotlib import colors
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from psychrochart import PsychroChart
import seaborn as sns

TITLE_FONTSIZE = 35
LABELS_FONTSIZE = 20
TICKS_FONTSIZE = 15
LEGEND_FONTSIZE = 15


def air_temperature(weather):
    fig, ax1 = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)
    ax2 = ax1.twinx()

    # add x, y gridlines
    ax1.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    ax2.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    # temperatures' bins from -20°C to +50°C
    bins = np.arange(-20, 40)
    # the histogram of the air temperature
    n, bins, patches = ax1.hist(weather['temp_air'],
                                bins,
                                alpha=0.6,
                                edgecolor='black')

    # setting the color gradient for temperatures
    norm = colors.Normalize(bins.min(), bins.max())

    for b, p in zip(bins, patches):
        color = plt.cm.inferno(norm(b))
        p.set_facecolor(color)

    # the cumulative distribution
    ax2.plot(bins[1:], (np.cumsum(n) / np.sum(n)) * 100,
             linewidth=3,
             alpha=0.6)

    # title
    plt.title("Air Temperature", fontsize=TITLE_FONTSIZE)

    # style axes
    ax1.tick_params(labelsize=TICKS_FONTSIZE)
    ax2.tick_params(labelsize=TICKS_FONTSIZE)
    plt.xticks(np.arange(-20, 41, 2))
    ax1.set_xlabel("Dry Bulb Temperature, T_air [°C]",
                   fontsize=LABELS_FONTSIZE)
    ax1.set_ylabel("Hours [hr]", fontsize=LABELS_FONTSIZE)
    ax2.set_ylabel("Cumulative frequency [%]", fontsize=LABELS_FONTSIZE)

    # legend
    handles = [
        Rectangle((0, 0), 1, 1, color=plt.cm.inferno(0.5), ec="k"),
        Rectangle((0, 0), 1, 1, color='blue', alpha=0.6)
    ]
    labels = ["Dry bulb temperature", "Cumulative frequency"]
    plt.legend(handles, labels)

    fig.tight_layout()
    plt.show()


def relative_humidity(weather):
    fig, ax1 = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)

    ax2 = ax1.twinx()

    # add x, y gridlines
    ax1.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    ax2.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    # temperatures' bins from -20°C to +50°C
    bins = np.arange(0, 100, 10)
    # the histogram of the air temperature
    n, bins, patches = ax1.hist(weather['relative_humidity'],
                                bins,
                                alpha=0.6,
                                edgecolor='black')

    # setting the color gradient for temperatures
    norm = colors.Normalize(bins.min(), bins.max())

    for b, p in zip(bins, patches):
        color = plt.cm.Blues(norm(b))
        p.set_facecolor(color)

    # the cumulative distribution
    ax2.plot(bins[1:], (np.cumsum(n) / np.sum(n)) * 100,
             linewidth=3,
             alpha=0.6)

    # title
    plt.title("Relative Humidity", fontsize=TITLE_FONTSIZE)

    # style axes
    ax1.tick_params(labelsize=TICKS_FONTSIZE)
    ax2.tick_params(labelsize=TICKS_FONTSIZE)
    plt.xticks(np.arange(0, 101, 10))
    ax1.set_xlabel("Relative humidity, RH [%]", fontsize=LABELS_FONTSIZE)
    ax1.set_ylabel("Hours [hr]", fontsize=LABELS_FONTSIZE)
    ax2.set_ylabel("Cumulative frequency [%]", fontsize=LABELS_FONTSIZE)

    # legend
    handles = [
        Rectangle((0, 0), 1, 1, color=plt.cm.Blues(0.5), ec="k"),
        Rectangle((0, 0), 1, 1, color='blue', alpha=0.6)
    ]
    labels = ["Relative humidity", "Cumulative frequency"]
    plt.legend(handles, labels)

    fig.tight_layout()
    plt.show()


def horizontal_irradiance(weather):
    fig, ax1 = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)

    ax2 = ax1.twinx()

    # add x, y gridlines
    ax1.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    ax2.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    # temperatures' bins from -20°C to +50°C
    bins = np.arange(weather['ghi'].min(), weather['ghi'].max(), 25)
    # the histogram of the air temperature
    n, bins, patches = ax1.hist([i for i in weather['ghi'] if i > 0],
                                bins,
                                alpha=0.6,
                                edgecolor='black')

    # setting the color gradient for temperatures
    norm = colors.Normalize(bins.min(), bins.max())

    for b, p in zip(bins, patches):
        color = plt.cm.viridis(norm(b))
        p.set_facecolor(color)

    # the cumulative distribution
    ax2.plot(bins[1:], (np.cumsum(n) / np.sum(n)) * 100,
             linewidth=3,
             alpha=0.6)

    # title
    plt.title("Global Horizontal Irradiance", fontsize=TITLE_FONTSIZE)

    # style axes
    ax1.tick_params(labelsize=TICKS_FONTSIZE)
    ax2.tick_params(labelsize=TICKS_FONTSIZE)
    plt.xticks(np.arange(weather['ghi'].min(), weather['ghi'].max(), 50))
    ax1.set_xlabel("Global horizontal irradiance, G_t [W/m²]",
                   fontsize=LABELS_FONTSIZE)
    ax1.set_ylabel("Hours [hr]", fontsize=LABELS_FONTSIZE)
    ax2.set_ylabel("Cumulative frequency [%]", fontsize=LABELS_FONTSIZE)

    # legend
    handles = [
        Rectangle((0, 0), 1, 1, color=plt.cm.viridis(0.5), ec="k"),
        Rectangle((0, 0), 1, 1, color='blue', alpha=0.6)
    ]
    labels = ["Global horizontal irradiance", "Cumulative frequency"]
    plt.legend(handles, labels)

    fig.tight_layout()
    plt.show()


def heating_loads(cultural_e):
    fig, axs = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)

    # add x, y gridlines
    axs.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    power = cultural_e['QHEAT_1'].to_numpy()

    # convert from Joule to Watt
    power = power / 3.6

    # TODO move this to data cleanup
    power = np.append(power[730:-730], power[-730:])
    y = -np.sort(-power)

    plt.plot(range(0, len(y)), y, label="Supply Air Total")

    # style axes
    plt.xticks(np.arange(0, 9500, 500))
    axs.tick_params(labelsize=TICKS_FONTSIZE)
    axs.set_xlabel("Time [hr]", fontsize=LABELS_FONTSIZE)
    axs.set_ylabel("Power [kW]", fontsize=LABELS_FONTSIZE)

    plt.legend(fontsize=LEGEND_FONTSIZE)

    plt.show()


def cooling_loads(cultural_e):
    fig, axs = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)

    # add x, y gridlines
    axs.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    power = cultural_e['QCOOL_1'].to_numpy()
    # convert from Joule to Watt
    power = power / 3.6

    # TODO move this to data cleanup
    power = np.append(power[730:-730], power[-730:])

    sns.lineplot(data=-np.sort(-power))

    # style axes
    plt.xlabel("Time [hr]")
    plt.ylabel("Power [kW]")
    plt.xticks(np.arange(0, 9500, 500))

    plt.show()


def energy_balance():
    fig, axs = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)

    # add x, y gridlines
    axs.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    labels = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December'
    ]

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # d = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]
    # e = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]
    # f = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]

    width = 0.35
    axs.bar(labels, a, width, label='Transmission')
    # axs.bar(labels, b, width, bottom=a, label='Heat')
    # axs.bar(labels, c, width, bottom=a+b, label='Change internal energy')
    # axs.bar(labels, d, width, label='Ventilation')
    # axs.bar(labels, e, width, bottom=d, label='Cooling')
    # axs.bar(labels, f, width, bottom=d+e, label='Internal gain')

    axs.set_ylabel('Energy Demand [kWh]')
    axs.set_title('Energy Balance')
    axs.legend()

    plt.show()


def psychrochart():
    custom_style = {
        "figure": {
            "figsize": [16, 9],
            "base_fontsize": 12,
            "title": "Psychrochart",
            "x_label": None,
            "y_label": None,
            "partial_axis": False
        },
        "limits": {
            "range_temp_c": [0, 45],
            "range_humidity_g_kg": [0, 30],
            "altitude_m": 900,
            "step_temp": .5
        },
        "saturation": {
            "color": [0, .3, 1.],
            "linewidth": 2
        },
        "constant_rh": {
            "color": [0.0, 0.498, 1.0, .7],
            "linewidth": 2.5,
            "linestyle": ":"
        },
        "chart_params": {
            "with_constant_rh": True,
            "constant_rh_curves": [25, 50, 75],
            "constant_rh_labels": [25, 50, 75],
            "range_vol_m3_kg": [0.9, 1.],
            "constant_v_labels": [0.9, 0.94, 0.98],
            "with_constant_h": False,
            "with_constant_wet_temp": False,
            "with_zones": False
        }
    }

    chart = PsychroChart(custom_style)

    # Append zones:
    zones_conf = {
        "zones": [{
            "zone_type": "dbt-rh",
            "style": {
                "edgecolor": [1.0, 0.749, 0.0, 0.8],
                "facecolor": [1.0, 0.749, 0.0, 0.2],
                "linewidth": 2,
                "linestyle": "--"
            },
            "points_x": [23, 28],
            "points_y": [40, 60],
            "label": "Summer"
        }, {
            "zone_type": "dbt-rh",
            "style": {
                "edgecolor": [0.498, 0.624, 0.8],
                "facecolor": [0.498, 0.624, 1.0, 0.2],
                "linewidth": 2,
                "linestyle": "--"
            },
            "points_x": [18, 23],
            "points_y": [35, 55],
            "label": "Winter"
        }]
    }

    chart.append_zones(zones_conf)

    # Plot the chart
    chart.plot()

    # Add labelled points and conexions between points
    points = {
        'exterior': {
            'label': 'Exterior',
            'style': {
                'color': [0.855, 0.004, 0.278, 0.8],
                'marker': 'X',
                'markersize': 15
            },
            'xy': (31.06, 32.9)
        },
        'interior': {
            'label': 'Interior',
            'style': {
                'color': [0.592, 0.745, 0.051, 0.9],
                'marker': 'o',
                'markersize': 15
            },
            'xy': (29.42, 52.34)
        },
        'interior2': {
            'style': {
                'color': [0.592, 0.745, 0.051, 0.9],
                'marker': 'o',
                'markersize': 15
            },
            'xy': (25.42, 52.34)
        }
    }

    chart.plot_points_dbt_rh(points)
    # Add a legend
    chart.plot_legend(markerscale=.7,
                      frameon=False,
                      fontsize=10,
                      labelspacing=1.2)

    ax = chart.plot()
    ax.get_figure()
