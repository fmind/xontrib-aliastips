def aliastips_find(cmd):
    # create a list of tuple where values must be list of arguments (not function)
    tuples = ((k, ' '.join(v)) for k, v in aliases.items() if isinstance(v, list))
    # sort the tuple by value length (from most to least specific)
    tuples = sorted(tuples, key=lambda x: len(x[1]), reverse=True)

    # filter the list when the command starts with the alias value
    return (alias for alias in tuples if cmd.startswith(alias[1]))


@events.on_precommand
def aliastips_on_precommand(cmd):
    for alias, value in aliastips_find(cmd):
        print('Alias tip: {0}={1}'.format(alias, value))


def aliastips(args):
    for alias, value in aliastips_find(' '.join(args)):
        print('{0}={1}'.format(alias, value))


aliases['aliastips'] = aliastips
