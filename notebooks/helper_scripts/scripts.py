def analyze_cat_cat(df, var, target):
    """
    Returns a dataframe that crosstabs the target against var,
    after dropping 'unknown' values. Returns both absolute values
    as well as proportions within each group of var.
    
    df is the dataframe containing all the variables
    var is a string identifying the exogenous variable
    target is a string identifying the endogenous variable
    """

    results = df.groupby([var, target]) \
                .agg( {target: 'count'}) \
                .rename({target: 'N'}, axis=1) \
                .drop('unknown', axis=0, level=0, errors='ignore') \
                .drop('unknown', axis=0, level=1, errors='ignore')
    
    results['percent'] = results.groupby(level=0) \
                                .apply(lambda x: x / x.sum())
    
    return results

def plot_cat_target(series, ax, max_x=0.2, xerr=None):
    """Plots the target variable for each group in series on a horizontal bar chart.
    Includes several modifications to make the graph look good.
    Plots the chart on ax with max xlim of max_x and errorbars xerr (optional).
    """
    if xerr is None: series.plot.barh(stacked=True, ax=ax, color=(0.2, 0.4, 0.6, 0.6))
    else: series.plot.barh(stacked=True, ax=ax, color=(0.2, 0.4, 0.6, 0.6), xerr=xerr)
#     ax.set_xlabel('Proportion of Respondents', fontsize=15)
    ax.set_xlim(0, max_x)
    ax.get_xaxis().set_major_formatter(
        mpl.ticker.FuncFormatter(lambda x,p: str(int(x*100))+'%'))   #format the x-axis to percentages

    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy() 
        ax.annotate('{:.1f} %'.format(width*100), (p.get_x()+1.05*width, p.get_y()+.4*height), 
                    fontsize=15, fontweight='bold')
        
def analyze_cat_num(df, var, target):
    """
    Returns a dataframe that returns descriptive statistics for the 
    numerical target against var, after dropping 'unknown' values. 
    
    df is the dataframe containing all the variables
    var is a string identifying the exogenous variable
    target is a string identifying the endogenous variable
    """
    
    results = df.loc[~(df[target]==-1), [var, target]] \
                .groupby(var) \
                .describe() \
                .drop('unknown', axis=0, errors='ignore')
    
    results.columns = results.columns.droplevel()
    results['std_err'] = results['std'] / np.sqrt(results['count'])
    
    return results

def plot_num_target(series, ax, max_x=0.2, xerr=None, xlabel=None):
    """Plots the target variable for each group in series on a horizontal bar chart.
    Includes several modifications to make the graph look good.
    Plots the chart on ax with max xlim of max_x and errorbars xerr (optional).
    """
    if xerr is None: series.plot.barh(stacked=True, ax=ax, color=(0.2, 0.4, 0.6, 0.6))
    else: series.plot.barh(stacked=True, ax=ax, color=(0.2, 0.4, 0.6, 0.6), xerr=xerr)
    if xlabel is not None: ax.set_xlabel(xlabel, fontsize=15)
    ax.set_xlim(0, max_x)

    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy() 
        ax.annotate('{:.2f}'.format(width), (p.get_x()+1.05*width, p.get_y()+.8*height), 
                    fontsize=15, fontweight='bold')