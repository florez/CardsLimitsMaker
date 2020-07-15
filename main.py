from utils import readYaml, getArgs


if __name__ == "__main__":

    args = getArgs()
    configData = readYaml('./config.yml')

    print(configData)
