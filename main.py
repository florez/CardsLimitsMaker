from utils import readYaml, getArgs


if __name__ == "__main__":

    args = getArgs()
    print(args)
    configData = readYaml('./config.yml')

    print(configData)
