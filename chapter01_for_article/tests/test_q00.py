from src.q00 import reverse_string

def test00():
    assert reverse_string('stressed') == 'desserts'
    assert reverse_string('drawer') == 'reward'
    assert reverse_string('racecar') == 'racecar'
    assert reverse_string('madam') == 'madam'
    assert reverse_string('rotor') == 'rotor'
    assert reverse_string('deified') == 'deified'
    assert reverse_string('repaper') == 'repaper'
    assert reverse_string('reviver') == 'reviver'
    assert reverse_string('civic') == 'civic'
    assert reverse_string('level') == 'level'
    assert reverse_string('radar') == 'radar'
    assert reverse_string('solos') == 'solos'
    assert reverse_string('stats') == 'stats'
    assert reverse_string('tenet') == 'tenet'
    assert reverse_string('refer') == 'refer'
    assert reverse_string('reifier') == 'reifier'
    assert reverse_string('rotator') == 'rotator'
    assert reverse_string('repaper') == 'repaper'
    assert reverse_string('reviver') == 'reviver'
    assert reverse_string('deified') == 'deified'
    assert reverse_string('rotor') == 'rotor'

    # 追加のテストケース
    assert reverse_string('') == ''
    assert reverse_string('!@#$$#@!') == '!@#$$#@!'
    assert reverse_string('1234567890') == '0987654321'
    assert reverse_string('AbCdEfG') == 'GfEdCbA'

    # 回文でないケースを追加
    assert reverse_string('hello') == 'olleh'
    assert reverse_string('world') == 'dlrow'
    assert reverse_string('python') == 'nohtyp'