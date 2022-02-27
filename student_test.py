import pytest
import student 



def test_inputs_specific_output():
    input_values=['3','4']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert output[2]==7

def test_inputs_all_output(capsys):
    input_values=['3','4']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.main()
    out,err =  capsys.readouterr()
    assert "7" in out



#Standard test output ONLY (no input)
#No need for the if __name__ condition in the main code, but might as well when done so students get used to it.
"""def test_hello(capsys):
    import hello
    out,err = capsys.readouterr()
    assert out == "Hello world!\n" or "bye" in out, "Should read 'Hello world!' "
"""

# Tests multiple values one at a time:

# def test_higher():
#     for i in [19, 91, 20, 24, 54, 33, 18]:
#         input_values=[str(i)]
#         output=[]

#         def mock_input(s=None):
#             if s is not None:
#                 output.append(s)
#                 return input_values.pop(0)
#             else:
#                 output.append("")
#                 return input_values.pop(0)
        
#         student.input = mock_input
#         student.print = lambda s : output.append(s)

#         student.main()

#         assert "true" in output[1].lower()
