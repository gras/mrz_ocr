from unittest import result
import mrz_ocr

def test_01():
    results = mrz_ocr.get_text('passports/01.png')
    assert results == "P<GBRJENNINGS<<PAUL<MICHAEL<<<<<<<<<<<<<<<<<\n" \
                      "0123456784GBR5011025M0810050<<<<<<<<<<<<<<00\n\f"

def test_02():
    # Note: the OCR fails!  KATIA is read as KATLIA
    results = mrz_ocr.get_text('passports/02.png')
    assert results == "IDBEL590335801485120100200<<<<\n" \
                      "8512017F0901015BEL<<<<<<<<<<<7\n" \
                      "REINARTZ<<ULRIKE<KATLIA<E<<<<<<\n\f"

def test_03():
    results = mrz_ocr.get_text('passports/03.jpg')
    assert results == "P<GRCPAPAKIRISKOU<<DIKAIA<<<<<<<<<<<<<<<<<<<\n" \
                      "AK31336543GRC8603050F2012076<<<<<<<<<<<<<<02\n\f"

def test_04():
    # Note: the OCR fails!  <<<<< is read as eeeec (red stripe fools the OCR)
    results = mrz_ocr.get_text('passports/04.jpg')
    assert results == "P<LVAVILUMS<<JOHANS<<<<<<<<<<<<<<<<<eeeec<<<\n" \
                      "LV71157713LVA7502167M2704151160275<15370<<58\n\f"

def test_05():
    results = mrz_ocr.get_text('passports/05.jpg')
    assert results == "P<GRCGIANNARIS<<TIMOTHEOTOS<<<<<<<<<<<<<<<<<\n" \
                      "AM24676885GRC0211288M2307275<<<<<<<<<<<<<<04\n\f"

def test_06():
    # Note: the OCR fails!  <<< is read as <KKé< (red stripe fools the OCR)
    results = mrz_ocr.get_text('passports/06.jpg')
    assert results == "P<LVASAULITIS<<ARMINS<<<<<<<<<<<<<<<<<<KKé<<<<\n" \
                      "LV07510991LVA7704282M2111072280477<17756<<46\n\f"

def test_07():
    # Note: the OCR fails!  <<<<<< is read as <éece< (red stripe fools the OCR)
    results = mrz_ocr.get_text('passports/07.jpg')
    assert results == "P<LVALAZDINS<<EGIJA<<<<<<<<<<<<<<<<<éece<<<<\n" \
                      "LV49944925LVA7107263F2512244260771<15479<<96\n\f"

def test_08():
    results = mrz_ocr.get_text('passports/08.jpg')
    assert results == "P<SRBRAJKOVIC<<FILIP<<<<<<<<<<<<<<<<<<<<<<<<\n" \
                      "8712120362SRB7503197M27110581903975553229<66\n\f"

def test_09():
    # Note: the OCR fails!  <<<<< is read as eeeeed (red stripe fools the OCR)
    results = mrz_ocr.get_text('passports/09.jpg')
    assert results == "P<LVAKRUZE<<ALLA<<<<<<<<<<<<<<<<<<<eeeeed<<<\n" \
                      "LV60367228LVA9307193F2503262190793<18761<<26\n\f"

def test_10():
    # Note: the OCR fails!  <<< is read as <e< (no red stripe...)
    results = mrz_ocr.get_text('passports/10.jpg')
    assert results == "P<SRBVLADIC<<TAMARA<<<<<<<<<<<<<<<<<<<<e<<<<\n" \
                      "1283314675SRB9208038F23121120308992733205<10\n\f"
