import pytest
import student 



def test_inputs():
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




#Standard test output ONLY (no input)
#No need for the if __name__ condition in the main code, but might as well when done so students get used to it.
"""def test_hello(capsys):
    import hello
    out,err = capsys.readouterr()
    assert out == "Hello world!\n" or "bye" in out, "Should read 'Hello world!' "
"""