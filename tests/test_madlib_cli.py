from madlib_cli.madlib import readTemplate,parse,merge

def test_readTemplate():
    actual = readTemplate('assets/test.txt')
    expected =f"""{{Ahmad}} is so annying when he tries to

solve the lab for a long time"""
    assert actual==expected

def test_parse():
    actual = parse(readTemplate('assets/test.txt'),ask_for_input=False)
    expected =['Ahmad']
    assert actual==expected

# I cant Because it require Input, I even tried to Overwrite The Input function But Without a use 

def test_merge():
    actual = merge(['Yassin'],readTemplate('assets/test.txt'))
    expected ="""Yassin is so annying when he tries to

solve the lab for a long time"""
    assert actual==expected