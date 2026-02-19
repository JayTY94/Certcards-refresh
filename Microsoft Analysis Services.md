1
Microsoft Analysis Services
Calculation groups can significantly reduce the number of redundant measures by having common measure expression patterns as calculation items. Calculation groups are supported in tabular models at the 1500 and higher compatibility level. This includes all Power BI semantic models.







2
Microsoft Analysis Services
For example, if you have 5 measures and want to create a prior year version for each you use the same pattern for each with the same DAX functions.

[Measure 1 Prior Year] = CALCULATE([Measure 1], PARALLELPERIOD('Date'[Date], -1, YEAR))
[Measure 2 Prior Year] = CALCULATE([Measure 2], PARALLELPERIOD('Date'[Date], -1, YEAR))
[Measure 3 Prior Year] = ...

Instead of creating 5 additional measures, you can use the pattern in a calculation item with a placeholder, SELECTEDMEASURE applying the expression to any measure.

CALCULATE(SELECTEDMEASURE(), PARALLELPERIOD('Date'[Date], -1, YEAR)





3
Microsoft Analysis Services
You can create a calculation group in the model view of Power BI Desktop or when editing a Power BI semantic model in the browser.

    Edit the semantic model
    Select Calculation group ribbon button.
    The first calculation item is created for you.
    Rename and adjust the expression.





4
Microsoft Analysis Services
Calculation groups are supported in Visual Studio with Analysis Services Projects VSIX update 2.9.2 and later. Calculation groups can also be created by using Tabular Model Scripting Language (TMSL) or the open source Tabular Editor.







5
Microsoft Analysis Services
Calculation groups address an issue in complex models where there can be a proliferation of redundant measures using the same calculations - most common with time intelligence calculations. For example, a sales analyst wants to view sales totals and orders by month-to-date (MTD), quarter-to-date (QTD), year-to-date (YTD), orders year-to-date for the previous year (PY), and so on.





6
Microsoft Analysis Services
Calculation groups are shown in reporting clients as a table with a single column. The column isn't like a typical column or dimension, instead it represents one or more reusable calculations, or calculation items that can be applied to any measure already added to the Values filter for a visualization.







7
Microsoft Analysis Services
Calculation groups don't work with implicit DAX measures. For example, in Power BI implicit measures are created when a user drags columns onto visuals to view aggregated values, without creating an explicit measure. At this time, Power BI generates DAX for implicit measures written as inline DAX calculations.





8
Microsoft Analysis Services
DAX functions specifically for calculation groups:

SELECTEDMEASURE - Used by expressions for calculation items to reference the measure that is currently in context. In this example, the Sales measure.

SELECTEDMEASURENAME - Used by expressions for calculation items to determine the measure that is in context by name.





9
Microsoft Analysis Services
DAX functions specifically for calculation groups:

ISSELECTEDMEASURE - Used by expressions for calculation items to determine the measure that is in context is specified in a list of measures.

SELECTEDMEASUREFORMATSTRING - Used by expressions for calculation items to retrieve the format string of the measure that is in context.





10
Microsoft Analysis Services
Dynamic format strings with calculation groups allow conditional application of format strings to measures without forcing them to return strings. Doing so has the potential to break some visuals.





11
Microsoft Analysis Services
Precedence is a property defined for a calculation group. It specifies the order the calculation groups are combined with the underlying measure when using SELECTEDMEASURE() in the calculation item.







12
Microsoft Analysis Services
For simple transformations, the evaluation is from lower to higher precedence. For example, 10 has 2 added, then it's multiplied by 2. In DAX, there are functions like CALCULATE that apply filters or context changes to inner expressions. In this case, the higher precedence alters a lower precedence expression.







13
Microsoft Analysis Services
By default, when a column from a calculation group is placed in a report, calculation items are ordered alphabetically by name. The order in which calculation items appear in a report can be changed by specifying the Ordinal property. 





14
Microsoft Analysis Services
Specifying calculation item order with the Ordinal property doesn't change precedence, the order in which calculation items are evaluated. It also doesn't change the order in which calculation items appear in Tabular Model Explorer.





15
Microsoft Analysis Services
To specify the ordinal property for calculation items, you must add a second column to the calculation group. Unlike the default column where Data Type is Text, a second column used for ordering calculation items has a Whole Number data type. 





16
Microsoft Analysis Services
As soon as a calculation group is added to a semantic model, Power BI reports will use the variant data type for all measures. If afterwards, all calculation groups are removed from the model the measures will be returned to their original data types again.







17
Microsoft Analysis Services
SQL Server Profiler, installed with SSMS, is a graphical user interface to SQL Trace for monitoring a server instance. You can capture and save data about each event to a file or table to analyze later.







18
Microsoft Analysis Services
SSMS includes extended events (xEvents), providing a lightweight alternative to SQL Server Profiler traces used for monitoring activity and diagnosing problems on Analysis Services servers. See Monitor Analysis Services with SQL Server Extended Events to learn more.







19
Microsoft Analysis Services
ALM Toolkit - An open-source schema compare tool for Power BI semantic models, most often used for application lifecycle management (ALM) scenarios. 
    Perform deployment across environments and retain incremental refresh historical data. 
    Diff and merge metadata files, branches and repos. 
    Reuse common definitions between models.





20
Microsoft Analysis Services
SQL Server Analysis Services (SSAS) provides several approaches, or modes, for creating business intelligence semantic models: Tabular and Multidimensional.







21
Microsoft Analysis Services
Multidimensional mode is only available with SQL Server Analysis Services. If you want your models deployed to Azure Analysis Services or Power BI, you can stop reading now. Multidimensional models will not be supported in Azure Analysis Services or Power BI Premium semantic models





22
Microsoft Analysis Services
An estimate used by many Analysis Services developers is that primary storage of a multidimensional database will be about one third size of the original data. Tabular databases can sometimes get greater amounts of compression, about one tenth the size, especially if most of the data is imported from fact tables.







23
Microsoft Analysis Services




s

24
Microsoft Analysis Services






25
Microsoft Analysis Services






26
Microsoft Analysis Services






27
Microsoft Analysis Services






28
Microsoft Analysis Services






29
Microsoft Analysis Services






30
Microsoft Analysis Services






31
Microsoft Analysis Services






32
Microsoft Analysis Services






33
Microsoft Analysis Services






34
Microsoft Analysis Services






35
Microsoft Analysis Services






36
Microsoft Analysis Services






37
Microsoft Analysis Services






38
Microsoft Analysis Services






39
Microsoft Analysis Services






40
Microsoft Analysis Services