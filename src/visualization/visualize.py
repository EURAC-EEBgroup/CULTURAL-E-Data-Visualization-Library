# -*- coding: utf-8 -*-
from matplotlib import colors
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Rectangle
import numpy as np
from psychrochart import PsychroChart, load_config
import seaborn as sns

# styling consants
TITLE_FONTSIZE = 32
LABELS_FONTSIZE = 20
TICKS_FONTSIZE = 15
LEGEND_FONTSIZE = 15
# conversion factors
JOULE_TO_WATT_FACTOR = 3.6
JOULE_TO_KW_FACTOR = JOULE_TO_WATT_FACTOR * 1000
HOURS_IN_A_MONTH = 730


def air_temperature(weather):
    '''
    Prints an histogram of the temperatures in the area during the year, plus their cumulative
    distribution.
    '''
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
        color = mpl.cm.inferno(norm(b))
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
    ax1.set_xlabel("Dry Bulb Temperature, T_out [°C]",
                   fontsize=LABELS_FONTSIZE)
    ax1.set_ylabel("Hours [hr]", fontsize=LABELS_FONTSIZE)
    ax2.set_ylabel("Cumulative frequency [%]", fontsize=LABELS_FONTSIZE)

    # legend
    handles = [
        Rectangle((0, 0), 1, 1, color=mpl.cm.inferno(0.5), ec="k"),
        Rectangle((0, 0), 1, 1, color='blue', alpha=0.6)
    ]
    labels = ["Dry bulb temperature", "Cumulative frequency"]
    plt.legend(handles, labels, fontsize=LEGEND_FONTSIZE)

    fig.tight_layout()
    plt.show()


def relative_humidity(weather):
    '''
    Prints an histogram of the relative humidity in the area during the year, plus its cumulative
    distribution.
    '''
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
        color = mpl.cm.Blues(norm(b))
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
        Rectangle((0, 0), 1, 1, color=mpl.cm.Blues(0.5), ec="k"),
        Rectangle((0, 0), 1, 1, color='blue', alpha=0.6)
    ]
    labels = ["Relative humidity", "Cumulative frequency"]
    plt.legend(handles, labels, fontsize=LEGEND_FONTSIZE)

    fig.tight_layout()
    plt.show()


def horizontal_irradiance(weather):
    '''
    Prints an histogram of the horizontal radiation in the area during the year.
    '''
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
        color = mpl.cm.viridis(norm(b))
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
        Rectangle((0, 0), 1, 1, color=mpl.cm.viridis(0.5), ec="k"),
        Rectangle((0, 0), 1, 1, color='blue', alpha=0.6)
    ]
    labels = ["Global horizontal irradiance", "Cumulative frequency"]
    plt.legend(handles, labels, fontsize=LEGEND_FONTSIZE)

    fig.tight_layout()
    plt.show()


def heating_loads(cultural_e):
    '''
    Prints the cumulative ideal loads of the heating system.
    '''
    _fig, axs = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)

    # add x, y gridlines
    axs.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    power = cultural_e['SQHEAT_1'].to_numpy()

    # convert from Joule to Watt
    power = power / JOULE_TO_WATT_FACTOR

    # sort by decreasing load
    y = -np.sort(-power)

    plt.plot(range(0, len(y)), y, label="Supply Air Total")

    # annotate max load
    label = "{:.2f}".format(y[0])
    plt.annotate(
        label,  # this is the text
        (0, y[0]),  # this is the point to label
        textcoords="offset points",  # how to position the text
        xytext=(0, 10),  # distance from text to points (x,y)
        ha='center',  # horizontal alignment can be left, right or center
        fontsize=LEGEND_FONTSIZE)

    # title
    plt.title("Cumulative Ideal Loads Heating Rate", fontsize=TITLE_FONTSIZE)

    # style axes
    plt.xticks(np.arange(0, 9500, 500))
    axs.tick_params(labelsize=TICKS_FONTSIZE)
    axs.set_xlabel("Time [hr]", fontsize=LABELS_FONTSIZE)
    axs.set_ylabel("Power [kW]", fontsize=LABELS_FONTSIZE)

    plt.legend(fontsize=LEGEND_FONTSIZE)

    plt.show()


def cooling_loads(cultural_e):
    '''
    Prints the cumulative ideal loads of the cooling system.
    '''
    _fig, axs = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)

    # add x, y gridlines
    axs.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    power = cultural_e['SQCOOL_1'].to_numpy()
    # convert from Joule to Watt
    power = power / JOULE_TO_WATT_FACTOR

    # sort by decreasing load
    y = -np.sort(-power)

    plt.plot(range(0, len(y)), y, label="Supply Air Total")

    # annotate max load
    label = "{:.2f}".format(y[0])
    plt.annotate(
        label,  # this is the text
        (0, y[0]),  # this is the point to label
        textcoords="offset points",  # how to position the text
        xytext=(0, 10),  # distance from text to points (x,y)
        ha='center',  # horizontal alignment can be left, right or center
        fontsize=LEGEND_FONTSIZE)

    # title
    plt.title("Cumulative Ideal Loads Cooling Rate", fontsize=TITLE_FONTSIZE)

    # style axes
    plt.xticks(np.arange(0, 9500, 500))
    axs.tick_params(labelsize=TICKS_FONTSIZE)
    axs.set_xlabel("Time [hr]", fontsize=LABELS_FONTSIZE)
    axs.set_ylabel("Power [kW]", fontsize=LABELS_FONTSIZE)

    plt.legend(fontsize=LEGEND_FONTSIZE)

    plt.show()


def energy_balance(balance):
    '''
    Prints the energy balance of the whole simulation.
    '''
    _fig, axs = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)

    # add x, y gridlines
    axs.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    # fields accounting for the energy balance
    fields = [
        'QHEAT', 'QCOOL', 'QINF', 'QVENT', 'QCOUPL', 'QTRANS', 'QGAININT',
        'QWGAIN', 'QSOLGAIN', 'QSOLAIR'
    ]

    # x axis contains the different zones simulated
    x = balance['Zonenr'].to_list()

    # first plot the positive contributions
    bottom = len(balance['Zonenr']) * [0]
    for _idx, name in enumerate(fields):
        plt.bar(x, [max(0, i) / JOULE_TO_KW_FACTOR for i in balance[name]],
                bottom=bottom,
                label=name)
        bottom = [
            max(0, i) / JOULE_TO_KW_FACTOR + j
            for i, j in zip(balance[name], bottom)
        ]

    # now plot the negative contributions
    bottom = len(balance['Zonenr']) * [0]
    for _idx, name in enumerate(fields):
        bottom = [
            min(0, i) / JOULE_TO_KW_FACTOR + j
            for i, j in zip(balance[name], bottom)
        ]
        plt.bar(x, [-min(0, i) / JOULE_TO_KW_FACTOR for i in balance[name]],
                bottom=bottom,
                label=name)

    # remove spines
    axs.spines['right'].set_visible(False)
    axs.spines['left'].set_visible(False)
    axs.spines['top'].set_visible(False)
    axs.spines['bottom'].set_visible(False)

    # style graph
    axs.set_title('Zone\'s Energy Balance', fontsize=TITLE_FONTSIZE)
    axs.set_ylabel('Energy Demand [kWh]', fontsize=LABELS_FONTSIZE)
    axs.set_xlabel("Zone", fontsize=LABELS_FONTSIZE)
    axs.tick_params(labelsize=TICKS_FONTSIZE)
    axs.legend(fontsize=LEGEND_FONTSIZE)

    plt.show()


import random


def zone_energy_balance(energy, zone=''):
    '''
    Print the energy balance of a single zone simulated.
    '''
    _fig, axs = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)

    # add x, y gridlines
    axs.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    labels = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December'
    ]

    # map hours to their month
    def month_from_hr(hour):
        return min(int(hour) // HOURS_IN_A_MONTH, len(labels) - 1)

    energy['MONTH'] = energy['TIME'].apply(month_from_hr)

    data = energy.groupby('MONTH').sum()

    # fields accounting for the energy balance
    fields = [
        zone + prop for prop in [
            '_B4_QBAL', '_B4_DQAIRdT', '_B4_QHEAT', '_B4_QCOOL', '_B4_QINF',
            '_B4_QVENT', 'B4_QCOUP', '_B4_QTRANS', '_B4_QGINT', '_B4_QWGAIN',
            '_B4_QSOL', '_B4_QSOLAIR'
        ]
    ]

    # the months of the year
    x = labels

    # first plot the positive contributions
    bottom = len(labels) * [0]
    for _idx, name in enumerate(fields):
        plt.bar(x, [max(0, i) / JOULE_TO_KW_FACTOR for i in data[name]],
                bottom=bottom,
                label=name)
        bottom = [
            max(0, i) / JOULE_TO_KW_FACTOR + j
            for i, j in zip(data[name], bottom)
        ]

    # now plot the negative contributions
    bottom = len(labels) * [0]
    for _idx, name in enumerate(fields):
        bottom = [
            min(0, i) / JOULE_TO_KW_FACTOR + j
            for i, j in zip(data[name], bottom)
        ]
        plt.bar(x, [-min(0, i) / JOULE_TO_KW_FACTOR for i in data[name]],
                bottom=bottom,
                label=name)

    # remove spines
    axs.spines['right'].set_visible(False)
    axs.spines['left'].set_visible(False)
    axs.spines['top'].set_visible(False)
    axs.spines['bottom'].set_visible(False)

    # style the graph
    axs.set_title('Monthly Energy Balance Zone: {}'.format(zone),
                  fontsize=TITLE_FONTSIZE)
    axs.set_ylabel('Energy Demand [kWh]', fontsize=LABELS_FONTSIZE)
    axs.tick_params(labelsize=TICKS_FONTSIZE)
    axs.legend(fontsize=LEGEND_FONTSIZE)

    plt.show()


def monthly_consumption(energy):
    '''
    Prints the consumpion in various categories.
    '''
    _fig, axs = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)

    # add x, y gridlines
    axs.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    labels = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December'
    ]

    # map hours to their month
    def month_from_hr(hour):
        return min(int(hour) // HOURS_IN_A_MONTH, len(labels) - 1)

    energy['MONTH'] = energy['TIME'].apply(month_from_hr)

    # aggregate monthly consumptions
    data = energy.groupby('MONTH').sum()

    # fields accounting for the consumtions
    fields = [
        'WEL_PDC_HEAT', 'WEL_PDC_COOL', 'WEL_VMC', 'IG_APL_TOT', 'IG_LGT_TOT'
    ]

    # months of the year
    x = labels

    # al the contributions should be positive, we currently ignore negative values
    bottom = len(labels) * [0]
    for _idx, name in enumerate(fields):
        plt.bar(x, [max(0, i) / JOULE_TO_KW_FACTOR for i in data[name]],
                bottom=bottom,
                label=name)
        bottom = [
            max(0, i) / JOULE_TO_KW_FACTOR + j
            for i, j in zip(data[name], bottom)
        ]

    # remove spines
    axs.spines['right'].set_visible(False)
    axs.spines['left'].set_visible(False)
    axs.spines['top'].set_visible(False)
    axs.spines['bottom'].set_visible(False)

    # style graph
    axs.set_title('Monthly Energy Consumption', fontsize=TITLE_FONTSIZE)
    axs.set_ylabel('Energy Demand [kWh]', fontsize=LABELS_FONTSIZE)
    axs.tick_params(labelsize=TICKS_FONTSIZE)
    axs.legend(fontsize=LEGEND_FONTSIZE)

    plt.show()


def self_production_consumption(energy):
    '''
    Prints the self-consumpion/self-production.
    '''
    _fig, axs = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)

    # the width of our bars
    bar_width = 0.3

    # add x, y gridlines
    axs.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    months = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December'
    ]

    # map hours to their month
    def month_from_hr(hour):
        return min(int(hour) // HOURS_IN_A_MONTH, len(months) - 1)

    energy['MONTH'] = energy['TIME'].apply(month_from_hr)

    # aggregate monthly consumptions
    data = energy.groupby('MONTH').sum()

    f_xpos = [i for i, _ in enumerate(months)]
    s_xpos = [val + bar_width for val in f_xpos]
    t_xpos = [val + bar_width for val in s_xpos]

    # we want to use months as our x-axis ticks, instead of numbers,
    # and we want it centered between the two bars.
    tick_pos = [val + bar_width for val in f_xpos]
    plt.xticks(tick_pos, months)

    #
    plt.bar(
        f_xpos,
        [max(0, i) / JOULE_TO_KW_FACTOR for i in data['Consumption_power']],
        label='Consumption',
        width=bar_width)
    plt.bar(s_xpos,
            [max(0, i) / JOULE_TO_KW_FACTOR for i in data['Production_power']],
            label='Production',
            width=bar_width)
    plt.bar(t_xpos, [
        max(0, i) / JOULE_TO_KW_FACTOR for i in data['Selfconsumption_power']
    ],
            label='Self-Consumption',
            width=bar_width)

    # remove spines
    axs.spines['right'].set_visible(False)
    axs.spines['left'].set_visible(False)
    axs.spines['top'].set_visible(False)
    axs.spines['bottom'].set_visible(False)

    # style graph
    axs.set_title('Self-Production/Self-Consumption', fontsize=TITLE_FONTSIZE)
    axs.set_ylabel('Energy Demand [kWh]', fontsize=LABELS_FONTSIZE)
    axs.tick_params(labelsize=TICKS_FONTSIZE)
    axs.legend(fontsize=LEGEND_FONTSIZE)

    plt.show()


def running_mean_outdoor_temperature(temp_array, alpha=0.8):
    """ Estimates the running mean temperature

    Parameters
    ----------
    temp_array: list
        array containing the mean daily temperature in descending order (i.e. from
        newest/yesterday to oldest) :math:`[\Theta_{day-1}, \Theta_{day-2}, \dots ,
        \Theta_{day-n}]`.
        Where :math:`\Theta_{day-1}` is yesterday's daily mean temperature. The EN
        16798-1 2019 [3]_ states that n should be equal to 7
    alpha : float
        constant between 0 and 1. The EN 16798-1 2019 [3]_ recommends a value of 0.8,
        while the ASHRAE 55 2017 recommends to choose values between 0.9 and 0.6,
        corresponding to a slow- and fast- response running mean, respectively.
        Adaptive comfort theory suggests that a slow-response running mean (alpha =
        0.9) could be more appropriate for climates in which synoptic-scale (day-to-
        day) temperature dynamics are relatively minor, such as the humid tropics.
    units: str default="SI"
        select the SI (International System of Units) or the IP (Imperial Units) system.

    Returns
    -------
    t_rm  : float
        running mean outdoor temperature
    """
    coeff = [alpha**ix for ix, x in enumerate(temp_array)]
    t_rm = sum([a * b for a, b in zip(coeff, temp_array)]) / sum(coeff)

    return round(t_rm, 1)


def adaptive_thermal_comfort():
    x = np.linspace(18, 30, 12)
    print(x)

    for c, l in [(-3, 'Cat III'), (-4, 'Cat II'), (-5, 'Cat I'), (2, 'Cat I'),
                 (3, 'Cat II'), (4, 'Cat III')]:
        y = 0.33 * x + 18.8 + c
        plt.plot(x, y, label=l)

    plt.legend()
    plt.show()


def psychrochart(data, zone, weather):
    '''
    Prints the standard Ashrae psychrometric chart with data from a zone.
    '''
    chart = PsychroChart('ashrae')

    # comfort zones
    zones_conf = {
        "zones": [{
            "zone_type": "dbt-rh",
            "style": {
                "edgecolor": [1.0, 0.749, 0.0],
                "facecolor": [1.0, 0.749, 0.0, 0.0],
                "linewidth": 5,
                "linestyle": "-"
            },
            "points_x": [23, 28],
            "points_y": [40, 60],
            "label": "Summer"
        }, {
            "zone_type": "dbt-rh",
            "style": {
                "edgecolor": [0.498, 0.624, 0.8],
                "facecolor": [1.0, 1.0, 1.0, 0.0],
                "linewidth": 5,
                "linestyle": "-"
            },
            "points_x": [18, 23],
            "points_y": [35, 55],
            "label": "Winter"
        }, {
            "zone_type": "dbt-rh",
            "style": {
                "edgecolor": [0.1, 0.1, 1.0],
                "facecolor": [0.1, 0.1, 1.0, 0.2],
                "linewidth": 2,
                "linestyle": "--"
            },
            "points_x": [0, 18],
            "points_y": [0, 100],
            "label": "Heating Zone"
        }, {
            "zone_type": "dbt-rh",
            "style": {
                "edgecolor": [1.00, 0.90, 0.40],
                "facecolor": [1.00, 0.90, 0.40, 0.2],
                "linewidth": 2,
                "linestyle": "--"
            },
            "points_x": [18, 50],
            "points_y": [0, 50],
            "label": "Cooling Humidifying Zone"
        }, {
            "zone_type": "dbt-rh",
            "style": {
                "edgecolor": [1.00, 0.16, 0.00],
                "facecolor": [1.00, 0.16, 0.00, 0.2],
                "linewidth": 2,
                "linestyle": "--"
            },
            "points_x": [18, 50],
            "points_y": [50, 100],
            "label": "Cooling Dehumidifying Zone"
        }]
    }

    chart.append_zones(zones_conf)

    # plot the chart together with the comfort zones
    ax = chart.plot()

    # add labelled points from the simulated zone
    points = dict()
    for index, row in data[['TAIR_' + zone, 'RELHUM_' + zone]].iterrows():
        key = 'interior_{}'.format(index)
        points.update({
            key: {
                'style': {
                    'color': [0.592, 0.745, 0.051, 1.0],
                    'marker': 'o',
                    'markersize': 8
                },
                'xy': (row['TAIR_' + zone], row['RELHUM_' + zone])
            }
        })

    chart.plot_points_dbt_rh(points)

    # add labelled points from outdoor conditions
    points = dict()
    for index, row in weather[['temp_air', 'relative_humidity']].iterrows():
        key = 'interior_{}'.format(index)
        points.update({
            key: {
                'style': {
                    'color': [0.992, 0.145, 0.051, 1.0],
                    'marker': 'x',
                    'markersize': 8
                },
                'xy': (row['temp_air'], row['relative_humidity'])
            }
        })

    chart.plot_points_dbt_rh(points)

    # Add a legend
    chart.plot_legend(markerscale=.7,
                      frameon=False,
                      fontsize=LEGEND_FONTSIZE,
                      labelspacing=1.2)

    return ax


def iaq_co2(data, living_rooms, bedrooms):
    '''
    Prints the indoor CO2 concentration belonging to four different classes of comfort.
    '''
    # average outdoor value for CO2
    OUTDOOR_CO2 = 400

    _fig, axs = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)

    # add x, y gridlines
    axs.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    # palette
    colors = ['#1D2F6F', '#8390FA', '#6EAF46', '#FAC748']

    # zones used during day have different categories with respect to nightly zones
    # start with day zones
    for zone in living_rooms:
        co2 = 'CO2_CON_' + zone
        occupancy = 'SCH_PER_' + zone

        co_2 = [
            data.query('({} <= {}) and ({} > 0)'.format(
                co2, OUTDOOR_CO2 + 550, occupancy))[co2].size
        ]
        co_2 = co_2 + [
            data.query('({} <= {}) and ({} > 0)'.format(
                co2, OUTDOOR_CO2 + 800, occupancy))[co2].size - sum(co_2)
        ]
        co_2 = co_2 + [
            data.query('({} <= {}) and ({} > 0)'.format(
                co2, OUTDOOR_CO2 + 1350, occupancy))[co2].size - sum(co_2)
        ]
        co_2 = co_2 + [
            data.query('({} > {}) and ({} > 0)'.format(co2, OUTDOOR_CO2 + 1350,
                                                       occupancy))[co2].size
        ]

        co_2 = [float(i) * 100 / sum(co_2) for i in co_2]

        plt.barh(co2, co_2[0], left=[0], color=colors[0])
        plt.barh(co2, co_2[1], left=co_2[0], color=colors[1])
        plt.barh(co2, co_2[2], left=sum(co_2[0:2]), color=colors[2])
        plt.barh(co2, co_2[3], left=sum(co_2[0:3]), color=colors[3])

    # follow with night zones
    for zone in bedrooms:
        co2 = 'CO2_CON_' + zone
        occupancy = 'SCH_PER_' + zone

        co_2 = [
            data.query('({} <= {}) and ({} > 0)'.format(
                co2, OUTDOOR_CO2 + 380, occupancy))[co2].size
        ]
        co_2 = co_2 + [
            data.query('({} <= {}) and ({} > 0)'.format(
                co2, OUTDOOR_CO2 + 550, occupancy))[co2].size - sum(co_2)
        ]
        co_2 = co_2 + [
            data.query('({} <= {}) and ({} > 0)'.format(
                co2, OUTDOOR_CO2 + 950, occupancy))[co2].size - sum(co_2)
        ]
        co_2 = co_2 + [
            data.query('({} > {}) and ({} > 0)'.format(co2, OUTDOOR_CO2 + 950,
                                                       occupancy))[co2].size
        ]

        co_2 = [float(i) * 100 / sum(co_2) for i in co_2]

        plt.barh(co2, co_2[0], left=[0], color=colors[0])
        plt.barh(co2, co_2[1], left=co_2[0], color=colors[1])
        plt.barh(co2, co_2[2], left=sum(co_2[0:2]), color=colors[2])
        plt.barh(co2, co_2[3], left=sum(co_2[0:3]), color=colors[3])

    # remove spines
    axs.spines['right'].set_visible(False)
    axs.spines['top'].set_visible(False)
    axs.spines['bottom'].set_visible(False)

    # style
    axs.set_title('Indoor Air Quality - CO2', fontsize=TITLE_FONTSIZE)
    axs.set_xlabel("Occupied Time [%]", fontsize=LABELS_FONTSIZE)
    axs.tick_params(labelsize=TICKS_FONTSIZE)
    labels = ['Category I', 'Category II', 'Category III', 'Category IV']
    axs.legend(labels, fontsize=LEGEND_FONTSIZE)

    plt.show()


def relh(data, zone_names, occupancy):
    '''

    '''
    _fig, axs = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)

    # add x, y gridlines
    axs.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

    colors = ['#1D2F6F', '#8390FA', '#6EAF46', '#FAC748']

    # in the case of relative humidity the comfort zones are intersecting
    # be aware that the order of the following lines is important
    for (zone, occ) in zip(zone_names, occupancy):
        relh = [
            data.query('({z} > 30) and ({z} < 50) and ({o} > 0)'.format(
                z=zone, o=occ))[zone].size
        ]
        relh = relh + [
            data.query('({z} > 20) and ({z} < 70) and ({o} > 0)'.format(
                z=zone, o=occ))[zone].size - sum(relh)
        ]
        relh = relh + [
            data.query('({z} > 70) and ({o} > 0)'.format(z=zone,
                                                         o=occ))[zone].size
        ]
        relh = relh + [
            data.query('({} < 20) and ({} > 0)'.format(zone, occ))[zone].size
        ]

        relh = [float(i) * 100 / sum(relh) for i in relh]

        plt.barh(zone, relh[0], left=[0], color=colors[0])
        plt.barh(zone, relh[1], left=relh[0], color=colors[1])
        plt.barh(zone, relh[2], left=sum(relh[0:2]), color=colors[2])
        plt.barh(zone, relh[3], left=sum(relh[0:3]), color=colors[3])

    # remove spines
    axs.spines['right'].set_visible(False)
    axs.spines['top'].set_visible(False)
    axs.spines['bottom'].set_visible(False)

    # style
    axs.set_title('Indoor Relative Humidity', fontsize=TITLE_FONTSIZE)
    axs.set_xlabel("Occupied Time [%]", fontsize=LABELS_FONTSIZE)
    axs.tick_params(labelsize=TICKS_FONTSIZE)
    labels = ['Category I', 'Category II', 'Too humid', 'Too dry']
    axs.legend(labels, fontsize=LEGEND_FONTSIZE)

    plt.show()


def airt_heatmap(data, zone):
    '''
    Prints a heatmap with the value for temperature at every hour of the day, for every day
    of the year.
    '''
    _fig, _axs = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)

    def hr_of_day(hour):
        return int(hour) % 24

    def day(hour):
        return int(hour) // 24

    # shape data
    df = data[['TIME', 'TAIR_' + zone]]
    df['DAY'] = df['TIME'].apply(day)
    df['HOUR'] = df['TIME'].apply(hr_of_day)
    df = df.pivot(index='HOUR', columns='DAY', values='TAIR_' + zone)

    sns.heatmap(df, cmap='plasma')

    plt.show()


def shd_heatmap(data):
    '''
    Prints a heatmap with the value for the shading at every hour of the day, for every day
    of the year.
    '''
    _fig, _axs = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)

    def hr_of_day(hour):
        return int(hour) % 24

    def day(hour):
        return int(hour) // 24

    # shape data
    df = data[['TIME', 'SHD_W1']]
    df['DAY'] = df['TIME'].apply(day)
    df['HOUR'] = df['TIME'].apply(hr_of_day)
    df = df.pivot(index='HOUR', columns='DAY', values='SHD_W1')
    sns.heatmap(df, cmap='plasma')

    plt.show()


def win_heatmap(data):
    '''
    Prints a heatmap with the value for the windows opening at every hour of the day, for every day
    of the year.
    '''
    _fig, _axs = plt.subplots(1, 1, figsize=(16, 9), tight_layout=True)

    def hr_of_day(hour):
        return int(hour) % 24

    def day(hour):
        return int(hour) // 24

    # shape data
    df = data[['TIME', 'WIN_LR']]
    df['DAY'] = df['TIME'].apply(day)
    df['HOUR'] = df['TIME'].apply(hr_of_day)
    df = df.pivot(index='HOUR', columns='DAY', values='WIN_LR')
    sns.heatmap(df, cmap='plasma')

    plt.show()
