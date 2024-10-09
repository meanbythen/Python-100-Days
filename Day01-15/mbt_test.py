time = 0


def calculate_average(numbers):
    """
    �����б������ֵ�ƽ��ֵ
    :param numbers: ������б�
    :return: �����б������ֵ�ƽ��ֵ
    """
    try:
        total = sum(numbers)  # �����б������ֵ��ܺ�,sum()����ֻ�����ڿɵ�������
        count = len(numbers)  # �����б������ֵĸ���
        average = total / count  # �����б������ֵ�ƽ��ֵ
    except AttributeError:  # �������Ĳ���һ���ɵ������󣬻��׳�AttributeError�쳣
        print("Error: Input is not a iterable object")
    except ZeroDivisionError:  # ���������б�Ϊ�գ����׳�ZeroDivisionError�쳣��������ƽ����0
        print('Input is a empty list')
        return 0
    except TypeError:  # ���������б��а���������ֵ�����׳�TypeError�쳣�������б���
        print("Error: Input contains non-numeric values")
        return numbers
    else:  # ���û���쳣���򷵻ؼ����ƽ��ֵ
        print(f"{numbers} Average Execute Success")
        return average
    finally:  # �����Ƿ����쳣������ִ��finally���飬ȫ�ֱ���time��1������Դ���������ӡ���Խ��
        global time
        time += 1
        print(f"The {time}th test result is:")


num1 = [1, 2, 3, 4, 5]
num2 = (1, 2, 3, 4, 5)
num3 = {1, 2, 3, 4, 5}
num4 = [1, 2, 'a', 4, 5]
num5 = []
num6 = 1
num7 = 3.14
num8 = [3.14, 1.73, 2.71, 1.41, 1.62]

testData = [num1, num2, num3, num4, num5, num6, num7, num8]
for index, numbers in enumerate(testData):
    average = calculate_average(numbers)
    print(f"{index + 1}:{numbers} average is:{average}")
