import datetime
import json
import functools
import numpy as np
from collections import OrderedDict
import matplotlib.pyplot as plt

features = ['alcohol',
            'chlorides',
            'citric acid',
            'density',
            'fixed acidity',
            'free sulfur dioxide',
            'pH',
            'residual sugar',
            'sulphates',
            'total sulfur dioxide',
            'volatile acidity']


statistics = ['min',
              'std',
              'max',
              'median',
              'mean']


def is_float(f):

    try:
        np.float64(f)
        return True
    except ValueError:
        return False


def is_valid_date(date):
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
        return True
    except ValueError:
        return False


def id_cmp(x, y):

    if x['id'] > y['id']:
        return 1
    else:
        return -1


def run_part_a(s):
    """
    s : string - the json string to be sorted

    returns: a list of dict ordered by vintage date, id
    """

    def sort_by_date_id(x, y):

        x_date = y_date = None
        x_date = datetime.datetime.strptime(x['vintage'], '%d/%m/%Y')
        y_date = datetime.datetime.strptime(y['vintage'], '%d/%m/%Y')

        if x_date == y_date:
            return id_cmp(x, y)
        elif x_date > y_date:
            return 1
        else:
            return -1

    # Filter invalid date entries.
    wine_list = list(filter(lambda w: is_valid_date(w["vintage"]), json.loads(str(s))))
    sorted_list = sorted(wine_list, key=functools.cmp_to_key(sort_by_date_id))
    return sorted_list


def run_part_b(s):
    """
    s : string - the json string

    returns :
    X : dtype float64 :
    a 2d numpy array with columns
                   'alcohol',
                   'chlorides',
                   'citric acid',
                   'density',
                   'fixed acidity',
                   'free sulfur dioxide',
                   'pH',
                   'residual sugar',
                   'sulphates',
                   'total sulfur dioxide',
                   'volatile acidity'
    y : dtype int64 : a 1d numpy array of quality
    """

    wine_list = json.loads(str(s))

    X = np.empty(shape=(1, 11), dtype=np.float64)
    X.fill(np.nan)
    y = np.array([], dtype=np.int64)

    first_feature = True
    filtered = 0

    for wine in wine_list:
        # Initialise coloum
        col = 0
        # Initialise feature array for wine with 'nan's
        x = np.empty(shape=(1, 11), dtype=np.float64)
        x.fill(np.nan)
        for feature in features:
            f = wine.get(feature, 'nan')
            filter_w = ['nan', 'null', 'none']
            # Iterate through each feature and ignore if not valid.
            if any(x in str(f).lower() for x in filter_w) or not is_float(f):
                continue
            else:
                x[0][col] = np.float64(f)
                col += 1

        quality = wine.get('quality', 'nan')
        # if we have both valid features and quality.
        if not np.any(np.isnan(x)) and quality != 'nan':
            # For the first feature just assign it.
            # TODO : Do a better way.
            if first_feature:
                X = x
                y = np.array(np.int64(quality))
                first_feature = False
            else:
                X = np.append(X, x, 0)
                y = np.append(y, np.int64(quality))
        else:
            # Not needed, Just for reference.
            filtered += 1
    return X, y


def run_part_c(s):
    """
    s : string - the json string

    returns a dict{string: date by year (or invalid), int (count of wines)}
    """

    wine_list = json.loads(str(s))
    wine_yearly_count = OrderedDict()

    for wine in wine_list:
        date = wine.get("vintage")
        if is_valid_date(date):
            year = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%Y')
        else:
            year = 'invalid'
        wine_yearly_count.setdefault(year, 0)
        wine_yearly_count[year] += 1

    return wine_yearly_count


def run_chart_c(d):
    """
    d: dict{string: date by year (or invalid), int (count of wines)}

    plots a chart showing counts of wine produced per dict entry
    """

    years = []
    count = []
    for index, k in enumerate(d):
        if k is not 'invalid':
            years.append(int(k))
            count.append(int(d[k]))

    plt.bar(years, count)
    plt.axis([2000, 2016, 80, 130])
    plt.xlabel('Years')
    plt.ylabel('Count')
    plt.title('Wine Production Chart')
    plt.savefig('result_charts/Wine Yearly Production Chart.png')


def run_part_d(s):
    """
    s : string - the json string

    d : a nested dict{ string - column : { string - statistic : value}}
    """
    x, _ = run_part_b(s)
    wine_statistics = OrderedDict()
    for dim, feature in enumerate(features):
        for stat in statistics:
            stat_ = eval('np.' + stat + '(x, axis=0)')[dim]
            stat_dict = OrderedDict([(stat,0.0)])
            wine_statistics.setdefault(feature, stat_dict)
            wine_statistics[feature][stat] = stat_

    return wine_statistics


def run_chart_d(d):
    """
    d : a nested dict{ string - column : { string - statistic : value}}

    plots a chart(s) showing plots of the statistics for each column
    """

    stat_array = []
    for feature, feature_stat in d.items():
        stat_array = [stat for _, stat in feature_stat.items()]
        plt.clf()
        plt.plot(list(range(10, 60, 10)), stat_array, 'go')
        plt.xticks(list(range(10, 60, 10)), statistics, rotation='vertical')
        plt.xlabel('Statistics')
        plt.title('Wine Statistics Chart - '+feature)
        plt.savefig('result_charts/Wine Statistics Chart - '+feature+'.png')
        stat_array.clear()
