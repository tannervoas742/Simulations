import sys

def FPrint(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()

def TableToText(Table): #TODO: Add title and header row
    if type(Table) == dict:
        return _TableToTextDict(Table)
    elif type(Table) == list:
        return _TableToTextList(Table)
    else:
        FPrint('ERROR: TableToText unsupported type! {}'.format(str(type(Table))))
        exit(1)

def _TableToTextDict(Table):
    Keys = list(sorted(list(Table.keys()), key=lambda x: str(x).lower().replace(' ', '')))
    Data = []
    for Key in Keys:
        Row = [str(Key) if type(Key) != str or '#' not in Key else Key.split('#')[1]]
        if type(Table[Key]) == list:
            Row += list(map(lambda x: str(x), Table[Key]))
        else:
            Row += [str(Table[Key])]
        Data += [Row]
    return _FormatTable(Data)

def _TableToTextList(Table):
    Data = []
    for Index in Table:
        Row = [list(map(lambda x: str(x), Table[Index]))]
        Data += [Row]
    return _FormatTable(Data)

def _FormatTable(Table):
    IndexSizes = {}
    for Row in Table:
        for Index in range(len(Row)):
            if Index not in IndexSizes:
                IndexSizes[Index] = len(Row[Index])
            elif len(Row[Index]) > IndexSizes[Index]:
                IndexSizes[Index] = len(Row[Index])
    for Row in Table:
        for Index in range(len(Row)):
            Row[Index] = ('{0:<' + '{}'.format(IndexSizes[Index]) + '}').format(Row[Index])
    Table = list(map(lambda Row: '| ' + ' | '.join(Row) + ' |', Table))
    RowLen = len(Table[0])
    Text = ' ' + '-' * (RowLen - 2) + ' ' + '\n'
    Text += '\n'.join(Table) + '\n'
    Text += ' ' + '-' * (RowLen - 2) + ' '
    return Text