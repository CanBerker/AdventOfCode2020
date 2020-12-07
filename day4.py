import re


def day4_part1(lines, mandatory_fields):
    passports = preprocess_input_into_passports(lines)
    count_passports_with_mandatory_fields = count_by_condition(doMandatoryFieldsExist)
    return count_passports_with_mandatory_fields(passports, mandatory_fields)


# BugNote for self, returned 195, submitted 194 and it worked
def day4_part2(lines, mandatory_fields):
    passports = preprocess_input_into_passports(lines)
    count_passports_with_mandatory_fields_and_valid_values = count_by_condition(isPassportValidForPart2)
    return count_passports_with_mandatory_fields_and_valid_values(passports, mandatory_fields)


def preprocess_input_into_passports(lines):
    passports = []
    passport = {}
    for line in lines:
        if len(line.strip()) == 0:
            passports.append(passport)
            passport = {}
            continue

        for entry in line.split(' '):
            key, value = entry.split(':')
            passport[key] = value.strip()

    passports.append(passport)
    return passports


def count_by_condition(condition_fn):
    def inner(passports, mandatory_fields):
        valid_passport_count = 0
        mandatory_fields = set(mandatory_fields)
        for passport in passports:
            if condition_fn(passport, mandatory_fields):
                valid_passport_count = valid_passport_count + 1
        return valid_passport_count

    return inner


def isPassportValidForPart2(passport, mandatory_fields):
    return doMandatoryFieldsExist(passport, mandatory_fields) and \
           areFieldValuesAreValid(passport)


def doMandatoryFieldsExist(passport, mandatory_fields):
    return mandatory_fields.issubset(set(passport.keys()))


def areFieldValuesAreValid(passport):
    is_valid = \
        isInRange(int(passport['byr']), 1920, 2002) and \
        isInRange(int(passport['iyr']), 2010, 2020) and \
        isInRange(int(passport['eyr']), 2020, 2030) and \
        isValidHeight(passport['hgt']) and \
        re.search('#[0-9a-f]{6}', passport['hcl']) is not None and \
        re.search('(amb|blu|brn|gry|grn|hzl|oth)', passport['ecl']) is not None and \
        re.search('[0-9]{9}', passport['pid']) is not None
    return is_valid


def isInRange(value, min_val, max_val):
    return min_val <= value <= max_val


def isValidHeight(height):
    if re.search('([0-9]{2}in)', height) is not None:
        value = int(height[:2])
        return 59 <= value <= 76
    if re.search('([0-9]{3}cm)', height) is not None:
        value = int(height[:3])
        return 150 <= value <= 193
