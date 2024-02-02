import datetime

from sqlalchemy import Boolean, Column, Float, Integer
from sqlalchemy.dialects.sqlite import DATETIME

from database import Base


class SET50Base():
    ADVANC = Column(Float)
    AOT = Column(Float)
    AWC = Column(Float)
    BANPU = Column(Float)
    BBL = Column(Float)
    BDMS = Column(Float)
    BEM = Column(Float)
    BGRIM = Column(Float)
    BH = Column(Float)
    BTS = Column(Float)
    CBG = Column(Float)
    CENTEL = Column(Float)
    COM7 = Column(Float)
    CPALL = Column(Float)
    CPF = Column(Float)
    CPN = Column(Float)
    CRC = Column(Float)
    DELTA = Column(Float)
    EA = Column(Float)
    EGCO = Column(Float)
    GLOBAL = Column(Float)
    GPSC = Column(Float)
    GULF = Column(Float)
    HMPRO = Column(Float)
    INTUCH = Column(Float)
    IVL = Column(Float)
    KBANK = Column(Float)
    KCE = Column(Float)
    KTB = Column(Float)
    KTC = Column(Float)
    LH = Column(Float)
    MINT = Column(Float)
    MTC = Column(Float)
    OR = Column(Float)
    OSP = Column(Float)
    PTT = Column(Float)
    PTTEP = Column(Float)
    PTTGC = Column(Float)
    RATCH = Column(Float)
    SAWAD = Column(Float)
    SCB = Column(Float)
    SCC = Column(Float)
    SCGP = Column(Float)
    TISCO = Column(Float)
    TLI = Column(Float)
    TOP = Column(Float)
    TRUE = Column(Float)
    TTB = Column(Float)
    TU = Column(Float)
    WHA = Column(Float)


class BacktestBase():
    ADVANC_test = Column(Float)
    AOT_test = Column(Float)
    AWC_test = Column(Float)
    BANPU_test = Column(Float)
    BBL_test = Column(Float)
    BDMS_test = Column(Float)
    BEM_test = Column(Float)
    BGRIM_test = Column(Float)
    BH_test = Column(Float)
    BTS_test = Column(Float)
    CBG_test = Column(Float)
    CENTEL_test = Column(Float)
    COM7_test = Column(Float)
    CPALL_test = Column(Float)
    CPF_test = Column(Float)
    CPN_test = Column(Float)
    CRC_test = Column(Float)
    DELTA_test = Column(Float)
    EA_test = Column(Float)
    EGCO_test = Column(Float)
    GLOBAL_test = Column(Float)
    GPSC_test = Column(Float)
    GULF_test = Column(Float)
    HMPRO_test = Column(Float)
    INTUCH_test = Column(Float)
    IVL_test = Column(Float)
    KBANK_test = Column(Float)
    KCE_test = Column(Float)
    KTB_test = Column(Float)
    KTC_test = Column(Float)
    LH_test = Column(Float)
    MINT_test = Column(Float)
    MTC_test = Column(Float)
    OR_test = Column(Float)
    OSP_test = Column(Float)
    PTT_test = Column(Float)
    PTTEP_test = Column(Float)
    PTTGC_test = Column(Float)
    RATCH_test = Column(Float)
    SAWAD_test = Column(Float)
    SCB_test = Column(Float)
    SCC_test = Column(Float)
    SCGP_test = Column(Float)
    TISCO_test = Column(Float)
    TLI_test = Column(Float)
    TOP_test = Column(Float)
    TRUE_test = Column(Float)
    TTB_test = Column(Float)
    TU_test = Column(Float)
    WHA_test = Column(Float)
    ADVANC_predict = Column(Float)
    AOT_predict = Column(Float)
    AWC_predict = Column(Float)
    BANPU_predict = Column(Float)
    BBL_predict = Column(Float)
    BDMS_predict = Column(Float)
    BEM_predict = Column(Float)
    BGRIM_predict = Column(Float)
    BH_predict = Column(Float)
    BTS_predict = Column(Float)
    CBG_predict = Column(Float)
    CENTEL_predict = Column(Float)
    COM7_predict = Column(Float)
    CPALL_predict = Column(Float)
    CPF_predict = Column(Float)
    CPN_predict = Column(Float)
    CRC_predict = Column(Float)
    DELTA_predict = Column(Float)
    EA_predict = Column(Float)
    EGCO_predict = Column(Float)
    GLOBAL_predict = Column(Float)
    GPSC_predict = Column(Float)
    GULF_predict = Column(Float)
    HMPRO_predict = Column(Float)
    INTUCH_predict = Column(Float)
    IVL_predict = Column(Float)
    KBANK_predict = Column(Float)
    KCE_predict = Column(Float)
    KTB_predict = Column(Float)
    KTC_predict = Column(Float)
    LH_predict = Column(Float)
    MINT_predict = Column(Float)
    MTC_predict = Column(Float)
    OR_predict = Column(Float)
    OSP_predict = Column(Float)
    PTT_predict = Column(Float)
    PTTEP_predict = Column(Float)
    PTTGC_predict = Column(Float)
    RATCH_predict = Column(Float)
    SAWAD_predict = Column(Float)
    SCB_predict = Column(Float)
    SCC_predict = Column(Float)
    SCGP_predict = Column(Float)
    TISCO_predict = Column(Float)
    TLI_predict = Column(Float)
    TOP_predict = Column(Float)
    TRUE_predict = Column(Float)
    TTB_predict = Column(Float)
    TU_predict = Column(Float)
    WHA_predict = Column(Float)


class BacktestStrategy():
    ADVANC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    ADVANC_close = Column(Float)
    ADVANC_ema_short = Column(Float)
    ADVANC_ema_long = Column(Float)
    ADVANC_buy_signal = Column(Boolean, unique=False, default=True)
    ADVANC_sell_signal = Column(Boolean, unique=False, default=True)
    ADVANC_green_signal = Column(Boolean, unique=False, default=True)
    ADVANC_red_signal = Column(Boolean, unique=False, default=True)
    AOT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    AOT_close = Column(Float)
    AOT_ema_short = Column(Float)
    AOT_ema_long = Column(Float)
    AOT_buy_signal = Column(Boolean, unique=False, default=True)
    AOT_sell_signal = Column(Boolean, unique=False, default=True)
    AOT_green_signal = Column(Boolean, unique=False, default=True)
    AOT_red_signal = Column(Boolean, unique=False, default=True)
    AWC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    AWC_close = Column(Float)
    AWC_ema_short = Column(Float)
    AWC_ema_long = Column(Float)
    AWC_buy_signal = Column(Boolean, unique=False, default=True)
    AWC_sell_signal = Column(Boolean, unique=False, default=True)
    AWC_green_signal = Column(Boolean, unique=False, default=True)
    AWC_red_signal = Column(Boolean, unique=False, default=True)
    BANPU_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BANPU_close = Column(Float)
    BANPU_ema_short = Column(Float)
    BANPU_ema_long = Column(Float)
    BANPU_buy_signal = Column(Boolean, unique=False, default=True)
    BANPU_sell_signal = Column(Boolean, unique=False, default=True)
    BANPU_green_signal = Column(Boolean, unique=False, default=True)
    BANPU_red_signal = Column(Boolean, unique=False, default=True)
    BBL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BBL_close = Column(Float)
    BBL_ema_short = Column(Float)
    BBL_ema_long = Column(Float)
    BBL_buy_signal = Column(Boolean, unique=False, default=True)
    BBL_sell_signal = Column(Boolean, unique=False, default=True)
    BBL_green_signal = Column(Boolean, unique=False, default=True)
    BBL_red_signal = Column(Boolean, unique=False, default=True)
    BDMS_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BDMS_close = Column(Float)
    BDMS_ema_short = Column(Float)
    BDMS_ema_long = Column(Float)
    BDMS_buy_signal = Column(Boolean, unique=False, default=True)
    BDMS_sell_signal = Column(Boolean, unique=False, default=True)
    BDMS_green_signal = Column(Boolean, unique=False, default=True)
    BDMS_red_signal = Column(Boolean, unique=False, default=True)
    BEM_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BEM_close = Column(Float)
    BEM_ema_short = Column(Float)
    BEM_ema_long = Column(Float)
    BEM_buy_signal = Column(Boolean, unique=False, default=True)
    BEM_sell_signal = Column(Boolean, unique=False, default=True)
    BEM_green_signal = Column(Boolean, unique=False, default=True)
    BEM_red_signal = Column(Boolean, unique=False, default=True)
    BGRIM_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BGRIM_close = Column(Float)
    BGRIM_ema_short = Column(Float)
    BGRIM_ema_long = Column(Float)
    BGRIM_buy_signal = Column(Boolean, unique=False, default=True)
    BGRIM_sell_signal = Column(Boolean, unique=False, default=True)
    BGRIM_green_signal = Column(Boolean, unique=False, default=True)
    BGRIM_red_signal = Column(Boolean, unique=False, default=True)
    BH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BH_close = Column(Float)
    BH_ema_short = Column(Float)
    BH_ema_long = Column(Float)
    BH_buy_signal = Column(Boolean, unique=False, default=True)
    BH_sell_signal = Column(Boolean, unique=False, default=True)
    BH_green_signal = Column(Boolean, unique=False, default=True)
    BH_red_signal = Column(Boolean, unique=False, default=True)
    BTS_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BTS_close = Column(Float)
    BTS_ema_short = Column(Float)
    BTS_ema_long = Column(Float)
    BTS_buy_signal = Column(Boolean, unique=False, default=True)
    BTS_sell_signal = Column(Boolean, unique=False, default=True)
    BTS_green_signal = Column(Boolean, unique=False, default=True)
    BTS_red_signal = Column(Boolean, unique=False, default=True)
    CBG_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CBG_close = Column(Float)
    CBG_ema_short = Column(Float)
    CBG_ema_long = Column(Float)
    CBG_buy_signal = Column(Boolean, unique=False, default=True)
    CBG_sell_signal = Column(Boolean, unique=False, default=True)
    CBG_green_signal = Column(Boolean, unique=False, default=True)
    CBG_red_signal = Column(Boolean, unique=False, default=True)
    CENTEL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CENTEL_close = Column(Float)
    CENTEL_ema_short = Column(Float)
    CENTEL_ema_long = Column(Float)
    CENTEL_buy_signal = Column(Boolean, unique=False, default=True)
    CENTEL_sell_signal = Column(Boolean, unique=False, default=True)
    CENTEL_green_signal = Column(Boolean, unique=False, default=True)
    CENTEL_red_signal = Column(Boolean, unique=False, default=True)
    COM7_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    COM7_close = Column(Float)
    COM7_ema_short = Column(Float)
    COM7_ema_long = Column(Float)
    COM7_buy_signal = Column(Boolean, unique=False, default=True)
    COM7_sell_signal = Column(Boolean, unique=False, default=True)
    COM7_green_signal = Column(Boolean, unique=False, default=True)
    COM7_red_signal = Column(Boolean, unique=False, default=True)
    CPALL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPALL_close = Column(Float)
    CPALL_ema_short = Column(Float)
    CPALL_ema_long = Column(Float)
    CPALL_buy_signal = Column(Boolean, unique=False, default=True)
    CPALL_sell_signal = Column(Boolean, unique=False, default=True)
    CPALL_green_signal = Column(Boolean, unique=False, default=True)
    CPALL_red_signal = Column(Boolean, unique=False, default=True)
    CPF_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPF_close = Column(Float)
    CPF_ema_short = Column(Float)
    CPF_ema_long = Column(Float)
    CPF_buy_signal = Column(Boolean, unique=False, default=True)
    CPF_sell_signal = Column(Boolean, unique=False, default=True)
    CPF_green_signal = Column(Boolean, unique=False, default=True)
    CPF_red_signal = Column(Boolean, unique=False, default=True)
    CPN_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPN_close = Column(Float)
    CPN_ema_short = Column(Float)
    CPN_ema_long = Column(Float)
    CPN_buy_signal = Column(Boolean, unique=False, default=True)
    CPN_sell_signal = Column(Boolean, unique=False, default=True)
    CPN_green_signal = Column(Boolean, unique=False, default=True)
    CPN_red_signal = Column(Boolean, unique=False, default=True)
    CRC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CRC_close = Column(Float)
    CRC_ema_short = Column(Float)
    CRC_ema_long = Column(Float)
    CRC_buy_signal = Column(Boolean, unique=False, default=True)
    CRC_sell_signal = Column(Boolean, unique=False, default=True)
    CRC_green_signal = Column(Boolean, unique=False, default=True)
    CRC_red_signal = Column(Boolean, unique=False, default=True)
    DELTA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    DELTA_close = Column(Float)
    DELTA_ema_short = Column(Float)
    DELTA_ema_long = Column(Float)
    DELTA_buy_signal = Column(Boolean, unique=False, default=True)
    DELTA_sell_signal = Column(Boolean, unique=False, default=True)
    DELTA_green_signal = Column(Boolean, unique=False, default=True)
    DELTA_red_signal = Column(Boolean, unique=False, default=True)
    EA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    EA_close = Column(Float)
    EA_ema_short = Column(Float)
    EA_ema_long = Column(Float)
    EA_buy_signal = Column(Boolean, unique=False, default=True)
    EA_sell_signal = Column(Boolean, unique=False, default=True)
    EA_green_signal = Column(Boolean, unique=False, default=True)
    EA_red_signal = Column(Boolean, unique=False, default=True)
    EGCO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    EGCO_close = Column(Float)
    EGCO_ema_short = Column(Float)
    EGCO_ema_long = Column(Float)
    EGCO_buy_signal = Column(Boolean, unique=False, default=True)
    EGCO_sell_signal = Column(Boolean, unique=False, default=True)
    EGCO_green_signal = Column(Boolean, unique=False, default=True)
    EGCO_red_signal = Column(Boolean, unique=False, default=True)
    GLOBAL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GLOBAL_close = Column(Float)
    GLOBAL_ema_short = Column(Float)
    GLOBAL_ema_long = Column(Float)
    GLOBAL_buy_signal = Column(Boolean, unique=False, default=True)
    GLOBAL_sell_signal = Column(Boolean, unique=False, default=True)
    GLOBAL_green_signal = Column(Boolean, unique=False, default=True)
    GLOBAL_red_signal = Column(Boolean, unique=False, default=True)
    GPSC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GPSC_close = Column(Float)
    GPSC_ema_short = Column(Float)
    GPSC_ema_long = Column(Float)
    GPSC_buy_signal = Column(Boolean, unique=False, default=True)
    GPSC_sell_signal = Column(Boolean, unique=False, default=True)
    GPSC_green_signal = Column(Boolean, unique=False, default=True)
    GPSC_red_signal = Column(Boolean, unique=False, default=True)
    GULF_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GULF_close = Column(Float)
    GULF_ema_short = Column(Float)
    GULF_ema_long = Column(Float)
    GULF_buy_signal = Column(Boolean, unique=False, default=True)
    GULF_sell_signal = Column(Boolean, unique=False, default=True)
    GULF_green_signal = Column(Boolean, unique=False, default=True)
    GULF_red_signal = Column(Boolean, unique=False, default=True)
    HMPRO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    HMPRO_close = Column(Float)
    HMPRO_ema_short = Column(Float)
    HMPRO_ema_long = Column(Float)
    HMPRO_buy_signal = Column(Boolean, unique=False, default=True)
    HMPRO_sell_signal = Column(Boolean, unique=False, default=True)
    HMPRO_green_signal = Column(Boolean, unique=False, default=True)
    HMPRO_red_signal = Column(Boolean, unique=False, default=True)
    INTUCH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    INTUCH_close = Column(Float)
    INTUCH_ema_short = Column(Float)
    INTUCH_ema_long = Column(Float)
    INTUCH_buy_signal = Column(Boolean, unique=False, default=True)
    INTUCH_sell_signal = Column(Boolean, unique=False, default=True)
    INTUCH_green_signal = Column(Boolean, unique=False, default=True)
    INTUCH_red_signal = Column(Boolean, unique=False, default=True)
    IVL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    IVL_close = Column(Float)
    IVL_ema_short = Column(Float)
    IVL_ema_long = Column(Float)
    IVL_buy_signal = Column(Boolean, unique=False, default=True)
    IVL_sell_signal = Column(Boolean, unique=False, default=True)
    IVL_green_signal = Column(Boolean, unique=False, default=True)
    IVL_red_signal = Column(Boolean, unique=False, default=True)
    KBANK_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KBANK_close = Column(Float)
    KBANK_ema_short = Column(Float)
    KBANK_ema_long = Column(Float)
    KBANK_buy_signal = Column(Boolean, unique=False, default=True)
    KBANK_sell_signal = Column(Boolean, unique=False, default=True)
    KBANK_green_signal = Column(Boolean, unique=False, default=True)
    KBANK_red_signal = Column(Boolean, unique=False, default=True)
    KCE_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KCE_close = Column(Float)
    KCE_ema_short = Column(Float)
    KCE_ema_long = Column(Float)
    KCE_buy_signal = Column(Boolean, unique=False, default=True)
    KCE_sell_signal = Column(Boolean, unique=False, default=True)
    KCE_green_signal = Column(Boolean, unique=False, default=True)
    KCE_red_signal = Column(Boolean, unique=False, default=True)
    KTB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KTB_close = Column(Float)
    KTB_ema_short = Column(Float)
    KTB_ema_long = Column(Float)
    KTB_buy_signal = Column(Boolean, unique=False, default=True)
    KTB_sell_signal = Column(Boolean, unique=False, default=True)
    KTB_green_signal = Column(Boolean, unique=False, default=True)
    KTB_red_signal = Column(Boolean, unique=False, default=True)
    KTC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KTC_close = Column(Float)
    KTC_ema_short = Column(Float)
    KTC_ema_long = Column(Float)
    KTC_buy_signal = Column(Boolean, unique=False, default=True)
    KTC_sell_signal = Column(Boolean, unique=False, default=True)
    KTC_green_signal = Column(Boolean, unique=False, default=True)
    KTC_red_signal = Column(Boolean, unique=False, default=True)
    LH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    LH_close = Column(Float)
    LH_ema_short = Column(Float)
    LH_ema_long = Column(Float)
    LH_buy_signal = Column(Boolean, unique=False, default=True)
    LH_sell_signal = Column(Boolean, unique=False, default=True)
    LH_green_signal = Column(Boolean, unique=False, default=True)
    LH_red_signal = Column(Boolean, unique=False, default=True)
    MINT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    MINT_close = Column(Float)
    MINT_ema_short = Column(Float)
    MINT_ema_long = Column(Float)
    MINT_buy_signal = Column(Boolean, unique=False, default=True)
    MINT_sell_signal = Column(Boolean, unique=False, default=True)
    MINT_green_signal = Column(Boolean, unique=False, default=True)
    MINT_red_signal = Column(Boolean, unique=False, default=True)
    MTC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    MTC_close = Column(Float)
    MTC_ema_short = Column(Float)
    MTC_ema_long = Column(Float)
    MTC_buy_signal = Column(Boolean, unique=False, default=True)
    MTC_sell_signal = Column(Boolean, unique=False, default=True)
    MTC_green_signal = Column(Boolean, unique=False, default=True)
    MTC_red_signal = Column(Boolean, unique=False, default=True)
    OR_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    OR_close = Column(Float)
    OR_ema_short = Column(Float)
    OR_ema_long = Column(Float)
    OR_buy_signal = Column(Boolean, unique=False, default=True)
    OR_sell_signal = Column(Boolean, unique=False, default=True)
    OR_green_signal = Column(Boolean, unique=False, default=True)
    OR_red_signal = Column(Boolean, unique=False, default=True)
    OSP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    OSP_close = Column(Float)
    OSP_ema_short = Column(Float)
    OSP_ema_long = Column(Float)
    OSP_buy_signal = Column(Boolean, unique=False, default=True)
    OSP_sell_signal = Column(Boolean, unique=False, default=True)
    OSP_green_signal = Column(Boolean, unique=False, default=True)
    OSP_red_signal = Column(Boolean, unique=False, default=True)
    PTT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTT_close = Column(Float)
    PTT_ema_short = Column(Float)
    PTT_ema_long = Column(Float)
    PTT_buy_signal = Column(Boolean, unique=False, default=True)
    PTT_sell_signal = Column(Boolean, unique=False, default=True)
    PTT_green_signal = Column(Boolean, unique=False, default=True)
    PTT_red_signal = Column(Boolean, unique=False, default=True)
    PTTEP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTTEP_close = Column(Float)
    PTTEP_ema_short = Column(Float)
    PTTEP_ema_long = Column(Float)
    PTTEP_buy_signal = Column(Boolean, unique=False, default=True)
    PTTEP_sell_signal = Column(Boolean, unique=False, default=True)
    PTTEP_green_signal = Column(Boolean, unique=False, default=True)
    PTTEP_red_signal = Column(Boolean, unique=False, default=True)
    PTTGC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTTGC_close = Column(Float)
    PTTGC_ema_short = Column(Float)
    PTTGC_ema_long = Column(Float)
    PTTGC_buy_signal = Column(Boolean, unique=False, default=True)
    PTTGC_sell_signal = Column(Boolean, unique=False, default=True)
    PTTGC_green_signal = Column(Boolean, unique=False, default=True)
    PTTGC_red_signal = Column(Boolean, unique=False, default=True)
    RATCH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    RATCH_close = Column(Float)
    RATCH_ema_short = Column(Float)
    RATCH_ema_long = Column(Float)
    RATCH_buy_signal = Column(Boolean, unique=False, default=True)
    RATCH_sell_signal = Column(Boolean, unique=False, default=True)
    RATCH_green_signal = Column(Boolean, unique=False, default=True)
    RATCH_red_signal = Column(Boolean, unique=False, default=True)
    SAWAD_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SAWAD_close = Column(Float)
    SAWAD_ema_short = Column(Float)
    SAWAD_ema_long = Column(Float)
    SAWAD_buy_signal = Column(Boolean, unique=False, default=True)
    SAWAD_sell_signal = Column(Boolean, unique=False, default=True)
    SAWAD_green_signal = Column(Boolean, unique=False, default=True)
    SAWAD_red_signal = Column(Boolean, unique=False, default=True)
    SCB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCB_close = Column(Float)
    SCB_ema_short = Column(Float)
    SCB_ema_long = Column(Float)
    SCB_buy_signal = Column(Boolean, unique=False, default=True)
    SCB_sell_signal = Column(Boolean, unique=False, default=True)
    SCB_green_signal = Column(Boolean, unique=False, default=True)
    SCB_red_signal = Column(Boolean, unique=False, default=True)
    SCC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCC_close = Column(Float)
    SCC_ema_short = Column(Float)
    SCC_ema_long = Column(Float)
    SCC_buy_signal = Column(Boolean, unique=False, default=True)
    SCC_sell_signal = Column(Boolean, unique=False, default=True)
    SCC_green_signal = Column(Boolean, unique=False, default=True)
    SCC_red_signal = Column(Boolean, unique=False, default=True)
    SCGP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCGP_close = Column(Float)
    SCGP_ema_short = Column(Float)
    SCGP_ema_long = Column(Float)
    SCGP_buy_signal = Column(Boolean, unique=False, default=True)
    SCGP_sell_signal = Column(Boolean, unique=False, default=True)
    SCGP_green_signal = Column(Boolean, unique=False, default=True)
    SCGP_red_signal = Column(Boolean, unique=False, default=True)
    TISCO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TISCO_close = Column(Float)
    TISCO_ema_short = Column(Float)
    TISCO_ema_long = Column(Float)
    TISCO_buy_signal = Column(Boolean, unique=False, default=True)
    TISCO_sell_signal = Column(Boolean, unique=False, default=True)
    TISCO_green_signal = Column(Boolean, unique=False, default=True)
    TISCO_red_signal = Column(Boolean, unique=False, default=True)
    TOP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TOP_close = Column(Float)
    TOP_ema_short = Column(Float)
    TOP_ema_long = Column(Float)
    TOP_buy_signal = Column(Boolean, unique=False, default=True)
    TOP_sell_signal = Column(Boolean, unique=False, default=True)
    TOP_green_signal = Column(Boolean, unique=False, default=True)
    TOP_red_signal = Column(Boolean, unique=False, default=True)
    TRUE_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TRUE_close = Column(Float)
    TRUE_ema_short = Column(Float)
    TRUE_ema_long = Column(Float)
    TRUE_buy_signal = Column(Boolean, unique=False, default=True)
    TRUE_sell_signal = Column(Boolean, unique=False, default=True)
    TRUE_green_signal = Column(Boolean, unique=False, default=True)
    TRUE_red_signal = Column(Boolean, unique=False, default=True)
    TTB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TTB_close = Column(Float)
    TTB_ema_short = Column(Float)
    TTB_ema_long = Column(Float)
    TTB_buy_signal = Column(Boolean, unique=False, default=True)
    TTB_sell_signal = Column(Boolean, unique=False, default=True)
    TTB_green_signal = Column(Boolean, unique=False, default=True)
    TTB_red_signal = Column(Boolean, unique=False, default=True)
    TU_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TU_close = Column(Float)
    TU_ema_short = Column(Float)
    TU_ema_long = Column(Float)
    TU_buy_signal = Column(Boolean, unique=False, default=True)
    TU_sell_signal = Column(Boolean, unique=False, default=True)
    TU_green_signal = Column(Boolean, unique=False, default=True)
    TU_red_signal = Column(Boolean, unique=False, default=True)
    WHA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    WHA_close = Column(Float)
    WHA_ema_short = Column(Float)
    WHA_ema_long = Column(Float)
    WHA_buy_signal = Column(Boolean, unique=False, default=True)
    WHA_sell_signal = Column(Boolean, unique=False, default=True)
    WHA_green_signal = Column(Boolean, unique=False, default=True)
    WHA_red_signal = Column(Boolean, unique=False, default=True)


# ---------------- Close & Volume Model ----------------


class MergeClose15T(SET50Base, Base):
    __tablename__ = "merge_close_15t"
    id = Column(Integer, primary_key=True)
    datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d " +
        "%(hour)02d:%(minute)02d:%(second)02d"
    ), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<MergeClose15T id={self.id} datetime={self.datetime}>"


class MergeClose1H(SET50Base, Base):
    __tablename__ = "merge_close_1h"
    id = Column(Integer, primary_key=True)
    datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d " +
        "%(hour)02d:%(minute)02d:%(second)02d"
    ), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<MergeClose1H id={self.id} datetime={self.datetime}>"


class MergeClose4H(SET50Base, Base):
    __tablename__ = "merge_close_4h"
    id = Column(Integer, primary_key=True)
    datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d " +
        "%(hour)02d:%(minute)02d:%(second)02d"
    ), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<MergeClose4H id={self.id} datetime={self.datetime}>"


class MergeClose1D(SET50Base, Base):
    __tablename__ = "merge_close_1d"
    id = Column(Integer, primary_key=True)
    datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d " +
        "%(hour)02d:%(minute)02d:%(second)02d"
    ), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<MergeClose1D id={self.id} datetime={self.datetime}>"


class MergeVolume15T(SET50Base, Base):
    __tablename__ = "merge_volume_15t"
    id = Column(Integer, primary_key=True)
    datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d " +
        "%(hour)02d:%(minute)02d:%(second)02d"
    ), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<MergeVolume15T id={self.id} datetime={self.datetime}>"


class MergeVolume1H(SET50Base, Base):
    __tablename__ = "merge_volume_1h"
    id = Column(Integer, primary_key=True)
    datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d " +
        "%(hour)02d:%(minute)02d:%(second)02d"
    ), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<MergeVolume1H id={self.id} datetime={self.datetime}>"


class MergeVolume4H(SET50Base, Base):
    __tablename__ = "merge_volume_4h"
    id = Column(Integer, primary_key=True)
    datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d " +
        "%(hour)02d:%(minute)02d:%(second)02d"
    ), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<MergeVolume4H id={self.id} datetime={self.datetime}>"


class MergeVolume1D(SET50Base, Base):
    __tablename__ = "merge_volume_1d"
    id = Column(Integer, primary_key=True)
    datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d " +
        "%(hour)02d:%(minute)02d:%(second)02d"
    ), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<MergeVolume1D id={self.id} datetime={self.datetime}>"

# ---------------- ARIMA Model ----------------


class ARIMAClose15T(SET50Base, Base):
    __tablename__ = "arima_close_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<CloseArima15T id={self.id}>"


class ARIMAClose1H(SET50Base, Base):
    __tablename__ = "arima_close_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<CloseArima1H id={self.id}>"


class ARIMAClose4H(SET50Base, Base):
    __tablename__ = "arima_close_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<CloseArima4H id={self.id}>"


class ARIMAClose1D(SET50Base, Base):
    __tablename__ = "arima_close_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<CloseArima1d id={self.id}>"


class ARIMAVolume15T(SET50Base, Base):
    __tablename__ = "arima_volume_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaVolume15T id={self.id}>"


class ARIMAVolume1H(SET50Base, Base):
    __tablename__ = "arima_volume_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaVolume1H id={self.id}>"


class ARIMAVolume4H(SET50Base, Base):
    __tablename__ = "arima_volume_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaVolume4H id={self.id}>"


class ARIMAVolume1D(SET50Base, Base):
    __tablename__ = "arima_volume_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaVolume1D id={self.id}>"

# ------ Backtest ------


class ARIMACloseBacktest15T(BacktestBase, Base):
    __tablename__ = "arima_close_backtest_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaBacktestClose15T id={self.id}>"


class ARIMACloseBacktest1H(BacktestBase, Base):
    __tablename__ = "arima_close_backtest_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaBacktestClose1H id={self.id}>"


class ARIMACloseBacktest4H(BacktestBase, Base):
    __tablename__ = "arima_close_backtest_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaBacktestClose4H id={self.id}>"


class ARIMACloseBacktest1D(BacktestBase, Base):
    __tablename__ = "arima_close_backtest_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaBacktestClose1D id={self.id}>"

# ------ MSE ERROR ------


class ARIMAMSE15T(SET50Base, Base):
    __tablename__ = "arima_mse_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaMSE15t id={self.id}>"


class ARIMAMSE1H(SET50Base, Base):
    __tablename__ = "arima_mse_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaMSE1H id={self.id}>"


class ARIMAMSE4H(SET50Base, Base):
    __tablename__ = "arima_mse_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaMSE4H id={self.id}>"


class ARIMAMSE1D(SET50Base, Base):
    __tablename__ = "arima_mse_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaMSE1D id={self.id}>"

# ---------------- LSTM Model ----------------


class LSTMClose15T(SET50Base, Base):
    __tablename__ = "lstm_close_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<CloseLSTM15T id={self.id}>"


class LSTMClose1H(SET50Base, Base):
    __tablename__ = "lstm_close_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<CloseLSTM1H id={self.id}>"


class LSTMClose4H(SET50Base, Base):
    __tablename__ = "lstm_close_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<CloseLSTM4H id={self.id}>"


class LSTMClose1D(SET50Base, Base):
    __tablename__ = "lstm_close_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<CloseLSTM1d id={self.id}>"


class LSTMVolume15T(SET50Base, Base):
    __tablename__ = "lstm_volume_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMVolume15T id={self.id}>"


class LSTMVolume1H(SET50Base, Base):
    __tablename__ = "lstm_volume_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMVolume1H id={self.id}>"


class LSTMVolume4H(SET50Base, Base):
    __tablename__ = "lstm_volume_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMVolume4H id={self.id}>"


class LSTMVolume1D(SET50Base, Base):
    __tablename__ = "lstm_volume_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMVolume1D id={self.id}>"

# ------ Backtest ------


class LSTMCloseBacktest15T(BacktestBase, Base):
    __tablename__ = "lstm_close_backtest_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMBacktestClose15T id={self.id}>"


class LSTMCloseBacktest1H(BacktestBase, Base):
    __tablename__ = "lstm_close_backtest_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMBacktestClose1H id={self.id}>"


class LSTMCloseBacktest4H(BacktestBase, Base):
    __tablename__ = "lstm_close_backtest_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMBacktestClose4H id={self.id}>"


class LSTMCloseBacktest1D(BacktestBase, Base):
    __tablename__ = "lstm_close_backtest_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMBacktestClose1D id={self.id}>"

# ------ MSE ERROR ------


class LSTMMSE15T(SET50Base, Base):
    __tablename__ = "lstm_mse_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMMSE15t id={self.id}>"


class LSTMMSE1H(SET50Base, Base):
    __tablename__ = "lstm_mse_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMMSE1H id={self.id}>"


class LSTMMSE4H(SET50Base, Base):
    __tablename__ = "lstm_mse_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMMSE4H id={self.id}>"


class LSTMMSE1D(SET50Base, Base):
    __tablename__ = "lstm_mse_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMMSE1D id={self.id}>"


# -------- Backtest Strategy ----------

class EMACROSSClose15T(BacktestStrategy, Base):
    __tablename__ = "ema_cross_close_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose15T id={self.id}>"


class EMACROSSClose1H(BacktestStrategy, Base):
    __tablename__ = "ema_cross_close_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose1H id={self.id}>"


class EMACROSSClose4H(BacktestStrategy, Base):
    __tablename__ = "ema_cross_close_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose4H id={self.id}>"


class EMACROSSClose1D(BacktestStrategy, Base):
    __tablename__ = "ema_cross_close_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose1D id={self.id}>"
