import json

from azureml.core import Webservice


# def main1(service):
#     # Creating input data
#     print("Creating input data")
#     data = {"data": [[ 1,2,3,4 ], [ 10,9,8,7 ]]}
#     input_data = json.dumps(data)
#
#     # Calling webservice
#     print("Calling webservice")
#     output_data = service.run(input_data)
#     predictions = output_data.get("predict")
#     assert type(predictions) == list


def main(service):
    # Creating input data
    print("Creating input data")
    data = {"data": [[21, 916, 194, 451, 178]]}
    input_data = json.dumps(data)

    # Calling webservice
    print("Calling webservice")
    output_data = service.run(input_data)
    predictions = output_data.get("predict")
    assert type(predictions) == list


if __name__ == "__main__":
    main()
