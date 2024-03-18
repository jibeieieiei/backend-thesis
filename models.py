import datetime

from sqlalchemy import Boolean, Column, Float, Integer, String
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


class BacktestStrategyEMA():
    ADVANC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    ADVANC_open = Column(Float)
    ADVANC_high = Column(Float)
    ADVANC_low = Column(Float)
    ADVANC_close = Column(Float)
    ADVANC_volume = Column(Integer)
    ADVANC_ema_short = Column(Float)
    ADVANC_ema_long = Column(Float)
    ADVANC_buy_signal = Column(Boolean, unique=False, default=True)
    ADVANC_sell_signal = Column(Boolean, unique=False, default=True)
    ADVANC_green_signal = Column(Float)
    ADVANC_red_signal = Column(Float)
    AOT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    AOT_open = Column(Float)
    AOT_high = Column(Float)
    AOT_low = Column(Float)
    AOT_close = Column(Float)
    AOT_volume = Column(Integer)
    AOT_ema_short = Column(Float)
    AOT_ema_long = Column(Float)
    AOT_buy_signal = Column(Boolean, unique=False, default=True)
    AOT_sell_signal = Column(Boolean, unique=False, default=True)
    AOT_green_signal = Column(Float)
    AOT_red_signal = Column(Float)
    AWC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    AWC_open = Column(Float)
    AWC_high = Column(Float)
    AWC_low = Column(Float)
    AWC_close = Column(Float)
    AWC_volume = Column(Integer)
    AWC_ema_short = Column(Float)
    AWC_ema_long = Column(Float)
    AWC_buy_signal = Column(Boolean, unique=False, default=True)
    AWC_sell_signal = Column(Boolean, unique=False, default=True)
    AWC_green_signal = Column(Float)
    AWC_red_signal = Column(Float)
    BANPU_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BANPU_open = Column(Float)
    BANPU_high = Column(Float)
    BANPU_low = Column(Float)
    BANPU_close = Column(Float)
    BANPU_volume = Column(Integer)
    BANPU_ema_short = Column(Float)
    BANPU_ema_long = Column(Float)
    BANPU_buy_signal = Column(Boolean, unique=False, default=True)
    BANPU_sell_signal = Column(Boolean, unique=False, default=True)
    BANPU_green_signal = Column(Float)
    BANPU_red_signal = Column(Float)
    BBL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BBL_open = Column(Float)
    BBL_high = Column(Float)
    BBL_low = Column(Float)
    BBL_close = Column(Float)
    BBL_volume = Column(Integer)
    BBL_ema_short = Column(Float)
    BBL_ema_long = Column(Float)
    BBL_buy_signal = Column(Boolean, unique=False, default=True)
    BBL_sell_signal = Column(Boolean, unique=False, default=True)
    BBL_green_signal = Column(Float)
    BBL_red_signal = Column(Float)
    BDMS_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BDMS_open = Column(Float)
    BDMS_high = Column(Float)
    BDMS_low = Column(Float)
    BDMS_close = Column(Float)
    BDMS_volume = Column(Integer)
    BDMS_ema_short = Column(Float)
    BDMS_ema_long = Column(Float)
    BDMS_buy_signal = Column(Boolean, unique=False, default=True)
    BDMS_sell_signal = Column(Boolean, unique=False, default=True)
    BDMS_green_signal = Column(Float)
    BDMS_red_signal = Column(Float)
    BEM_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BEM_open = Column(Float)
    BEM_high = Column(Float)
    BEM_low = Column(Float)
    BEM_close = Column(Float)
    BEM_volume = Column(Integer)
    BEM_ema_short = Column(Float)
    BEM_ema_long = Column(Float)
    BEM_buy_signal = Column(Boolean, unique=False, default=True)
    BEM_sell_signal = Column(Boolean, unique=False, default=True)
    BEM_green_signal = Column(Float)
    BEM_red_signal = Column(Float)
    BGRIM_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BGRIM_open = Column(Float)
    BGRIM_high = Column(Float)
    BGRIM_low = Column(Float)
    BGRIM_close = Column(Float)
    BGRIM_volume = Column(Integer)
    BGRIM_ema_short = Column(Float)
    BGRIM_ema_long = Column(Float)
    BGRIM_buy_signal = Column(Boolean, unique=False, default=True)
    BGRIM_sell_signal = Column(Boolean, unique=False, default=True)
    BGRIM_green_signal = Column(Float)
    BGRIM_red_signal = Column(Float)
    BH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BH_open = Column(Float)
    BH_high = Column(Float)
    BH_low = Column(Float)
    BH_close = Column(Float)
    BH_volume = Column(Integer)
    BH_ema_short = Column(Float)
    BH_ema_long = Column(Float)
    BH_buy_signal = Column(Boolean, unique=False, default=True)
    BH_sell_signal = Column(Boolean, unique=False, default=True)
    BH_green_signal = Column(Float)
    BH_red_signal = Column(Float)
    BTS_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BTS_open = Column(Float)
    BTS_high = Column(Float)
    BTS_low = Column(Float)
    BTS_close = Column(Float)
    BTS_volume = Column(Integer)
    BTS_ema_short = Column(Float)
    BTS_ema_long = Column(Float)
    BTS_buy_signal = Column(Boolean, unique=False, default=True)
    BTS_sell_signal = Column(Boolean, unique=False, default=True)
    BTS_green_signal = Column(Float)
    BTS_red_signal = Column(Float)
    CBG_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CBG_open = Column(Float)
    CBG_high = Column(Float)
    CBG_low = Column(Float)
    CBG_close = Column(Float)
    CBG_volume = Column(Integer)
    CBG_ema_short = Column(Float)
    CBG_ema_long = Column(Float)
    CBG_buy_signal = Column(Boolean, unique=False, default=True)
    CBG_sell_signal = Column(Boolean, unique=False, default=True)
    CBG_green_signal = Column(Float)
    CBG_red_signal = Column(Float)
    CENTEL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CENTEL_open = Column(Float)
    CENTEL_high = Column(Float)
    CENTEL_low = Column(Float)
    CENTEL_close = Column(Float)
    CENTEL_volume = Column(Integer)
    CENTEL_ema_short = Column(Float)
    CENTEL_ema_long = Column(Float)
    CENTEL_buy_signal = Column(Boolean, unique=False, default=True)
    CENTEL_sell_signal = Column(Boolean, unique=False, default=True)
    CENTEL_green_signal = Column(Float)
    CENTEL_red_signal = Column(Float)
    COM7_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    COM7_open = Column(Float)
    COM7_high = Column(Float)
    COM7_low = Column(Float)
    COM7_close = Column(Float)
    COM7_volume = Column(Integer)
    COM7_ema_short = Column(Float)
    COM7_ema_long = Column(Float)
    COM7_buy_signal = Column(Boolean, unique=False, default=True)
    COM7_sell_signal = Column(Boolean, unique=False, default=True)
    COM7_green_signal = Column(Float)
    COM7_red_signal = Column(Float)
    CPALL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPALL_open = Column(Float)
    CPALL_high = Column(Float)
    CPALL_low = Column(Float)
    CPALL_close = Column(Float)
    CPALL_volume = Column(Integer)
    CPALL_ema_short = Column(Float)
    CPALL_ema_long = Column(Float)
    CPALL_buy_signal = Column(Boolean, unique=False, default=True)
    CPALL_sell_signal = Column(Boolean, unique=False, default=True)
    CPALL_green_signal = Column(Float)
    CPALL_red_signal = Column(Float)
    CPF_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPF_open = Column(Float)
    CPF_high = Column(Float)
    CPF_low = Column(Float)
    CPF_close = Column(Float)
    CPF_volume = Column(Integer)
    CPF_ema_short = Column(Float)
    CPF_ema_long = Column(Float)
    CPF_buy_signal = Column(Boolean, unique=False, default=True)
    CPF_sell_signal = Column(Boolean, unique=False, default=True)
    CPF_green_signal = Column(Float)
    CPF_red_signal = Column(Float)
    CPN_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPN_open = Column(Float)
    CPN_high = Column(Float)
    CPN_low = Column(Float)
    CPN_close = Column(Float)
    CPN_volume = Column(Integer)
    CPN_ema_short = Column(Float)
    CPN_ema_long = Column(Float)
    CPN_buy_signal = Column(Boolean, unique=False, default=True)
    CPN_sell_signal = Column(Boolean, unique=False, default=True)
    CPN_green_signal = Column(Float)
    CPN_red_signal = Column(Float)
    CRC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CRC_open = Column(Float)
    CRC_high = Column(Float)
    CRC_low = Column(Float)
    CRC_close = Column(Float)
    CRC_volume = Column(Integer)
    CRC_ema_short = Column(Float)
    CRC_ema_long = Column(Float)
    CRC_buy_signal = Column(Boolean, unique=False, default=True)
    CRC_sell_signal = Column(Boolean, unique=False, default=True)
    CRC_green_signal = Column(Float)
    CRC_red_signal = Column(Float)
    DELTA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    DELTA_open = Column(Float)
    DELTA_high = Column(Float)
    DELTA_low = Column(Float)
    DELTA_close = Column(Float)
    DELTA_volume = Column(Integer)
    DELTA_ema_short = Column(Float)
    DELTA_ema_long = Column(Float)
    DELTA_buy_signal = Column(Boolean, unique=False, default=True)
    DELTA_sell_signal = Column(Boolean, unique=False, default=True)
    DELTA_green_signal = Column(Float)
    DELTA_red_signal = Column(Float)
    EA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    EA_open = Column(Float)
    EA_high = Column(Float)
    EA_low = Column(Float)
    EA_close = Column(Float)
    EA_volume = Column(Integer)
    EA_ema_short = Column(Float)
    EA_ema_long = Column(Float)
    EA_buy_signal = Column(Boolean, unique=False, default=True)
    EA_sell_signal = Column(Boolean, unique=False, default=True)
    EA_green_signal = Column(Float)
    EA_red_signal = Column(Float)
    EGCO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    EGCO_open = Column(Float)
    EGCO_high = Column(Float)
    EGCO_low = Column(Float)
    EGCO_close = Column(Float)
    EGCO_volume = Column(Integer)
    EGCO_ema_short = Column(Float)
    EGCO_ema_long = Column(Float)
    EGCO_buy_signal = Column(Boolean, unique=False, default=True)
    EGCO_sell_signal = Column(Boolean, unique=False, default=True)
    EGCO_green_signal = Column(Float)
    EGCO_red_signal = Column(Float)
    GLOBAL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GLOBAL_open = Column(Float)
    GLOBAL_high = Column(Float)
    GLOBAL_low = Column(Float)
    GLOBAL_close = Column(Float)
    GLOBAL_volume = Column(Integer)
    GLOBAL_ema_short = Column(Float)
    GLOBAL_ema_long = Column(Float)
    GLOBAL_buy_signal = Column(Boolean, unique=False, default=True)
    GLOBAL_sell_signal = Column(Boolean, unique=False, default=True)
    GLOBAL_green_signal = Column(Float)
    GLOBAL_red_signal = Column(Float)
    GPSC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GPSC_open = Column(Float)
    GPSC_high = Column(Float)
    GPSC_low = Column(Float)
    GPSC_close = Column(Float)
    GPSC_volume = Column(Integer)
    GPSC_ema_short = Column(Float)
    GPSC_ema_long = Column(Float)
    GPSC_buy_signal = Column(Boolean, unique=False, default=True)
    GPSC_sell_signal = Column(Boolean, unique=False, default=True)
    GPSC_green_signal = Column(Float)
    GPSC_red_signal = Column(Float)
    GULF_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GULF_open = Column(Float)
    GULF_high = Column(Float)
    GULF_low = Column(Float)
    GULF_close = Column(Float)
    GULF_volume = Column(Integer)
    GULF_ema_short = Column(Float)
    GULF_ema_long = Column(Float)
    GULF_buy_signal = Column(Boolean, unique=False, default=True)
    GULF_sell_signal = Column(Boolean, unique=False, default=True)
    GULF_green_signal = Column(Float)
    GULF_red_signal = Column(Float)
    HMPRO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    HMPRO_open = Column(Float)
    HMPRO_high = Column(Float)
    HMPRO_low = Column(Float)
    HMPRO_close = Column(Float)
    HMPRO_volume = Column(Integer)
    HMPRO_ema_short = Column(Float)
    HMPRO_ema_long = Column(Float)
    HMPRO_buy_signal = Column(Boolean, unique=False, default=True)
    HMPRO_sell_signal = Column(Boolean, unique=False, default=True)
    HMPRO_green_signal = Column(Float)
    HMPRO_red_signal = Column(Float)
    INTUCH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    INTUCH_open = Column(Float)
    INTUCH_high = Column(Float)
    INTUCH_low = Column(Float)
    INTUCH_close = Column(Float)
    INTUCH_volume = Column(Integer)
    INTUCH_ema_short = Column(Float)
    INTUCH_ema_long = Column(Float)
    INTUCH_buy_signal = Column(Boolean, unique=False, default=True)
    INTUCH_sell_signal = Column(Boolean, unique=False, default=True)
    INTUCH_green_signal = Column(Float)
    INTUCH_red_signal = Column(Float)
    IVL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    IVL_open = Column(Float)
    IVL_high = Column(Float)
    IVL_low = Column(Float)
    IVL_close = Column(Float)
    IVL_volume = Column(Integer)
    IVL_ema_short = Column(Float)
    IVL_ema_long = Column(Float)
    IVL_buy_signal = Column(Boolean, unique=False, default=True)
    IVL_sell_signal = Column(Boolean, unique=False, default=True)
    IVL_green_signal = Column(Float)
    IVL_red_signal = Column(Float)
    KBANK_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KBANK_open = Column(Float)
    KBANK_high = Column(Float)
    KBANK_low = Column(Float)
    KBANK_close = Column(Float)
    KBANK_volume = Column(Integer)
    KBANK_ema_short = Column(Float)
    KBANK_ema_long = Column(Float)
    KBANK_buy_signal = Column(Boolean, unique=False, default=True)
    KBANK_sell_signal = Column(Boolean, unique=False, default=True)
    KBANK_green_signal = Column(Float)
    KBANK_red_signal = Column(Float)
    KCE_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KCE_open = Column(Float)
    KCE_high = Column(Float)
    KCE_low = Column(Float)
    KCE_close = Column(Float)
    KCE_volume = Column(Integer)
    KCE_ema_short = Column(Float)
    KCE_ema_long = Column(Float)
    KCE_buy_signal = Column(Boolean, unique=False, default=True)
    KCE_sell_signal = Column(Boolean, unique=False, default=True)
    KCE_green_signal = Column(Float)
    KCE_red_signal = Column(Float)
    KTB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KTB_open = Column(Float)
    KTB_high = Column(Float)
    KTB_low = Column(Float)
    KTB_close = Column(Float)
    KTB_volume = Column(Integer)
    KTB_ema_short = Column(Float)
    KTB_ema_long = Column(Float)
    KTB_buy_signal = Column(Boolean, unique=False, default=True)
    KTB_sell_signal = Column(Boolean, unique=False, default=True)
    KTB_green_signal = Column(Float)
    KTB_red_signal = Column(Float)
    KTC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KTC_open = Column(Float)
    KTC_high = Column(Float)
    KTC_low = Column(Float)
    KTC_close = Column(Float)
    KTC_volume = Column(Integer)
    KTC_ema_short = Column(Float)
    KTC_ema_long = Column(Float)
    KTC_buy_signal = Column(Boolean, unique=False, default=True)
    KTC_sell_signal = Column(Boolean, unique=False, default=True)
    KTC_green_signal = Column(Float)
    KTC_red_signal = Column(Float)
    LH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    LH_open = Column(Float)
    LH_high = Column(Float)
    LH_low = Column(Float)
    LH_close = Column(Float)
    LH_volume = Column(Integer)
    LH_ema_short = Column(Float)
    LH_ema_long = Column(Float)
    LH_buy_signal = Column(Boolean, unique=False, default=True)
    LH_sell_signal = Column(Boolean, unique=False, default=True)
    LH_green_signal = Column(Float)
    LH_red_signal = Column(Float)
    MINT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    MINT_open = Column(Float)
    MINT_high = Column(Float)
    MINT_low = Column(Float)
    MINT_close = Column(Float)
    MINT_volume = Column(Integer)
    MINT_ema_short = Column(Float)
    MINT_ema_long = Column(Float)
    MINT_buy_signal = Column(Boolean, unique=False, default=True)
    MINT_sell_signal = Column(Boolean, unique=False, default=True)
    MINT_green_signal = Column(Float)
    MINT_red_signal = Column(Float)
    MTC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    MTC_open = Column(Float)
    MTC_high = Column(Float)
    MTC_low = Column(Float)
    MTC_close = Column(Float)
    MTC_volume = Column(Integer)
    MTC_ema_short = Column(Float)
    MTC_ema_long = Column(Float)
    MTC_buy_signal = Column(Boolean, unique=False, default=True)
    MTC_sell_signal = Column(Boolean, unique=False, default=True)
    MTC_green_signal = Column(Float)
    MTC_red_signal = Column(Float)
    OR_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    OR_open = Column(Float)
    OR_high = Column(Float)
    OR_low = Column(Float)
    OR_close = Column(Float)
    OR_volume = Column(Integer)
    OR_ema_short = Column(Float)
    OR_ema_long = Column(Float)
    OR_buy_signal = Column(Boolean, unique=False, default=True)
    OR_sell_signal = Column(Boolean, unique=False, default=True)
    OR_green_signal = Column(Float)
    OR_red_signal = Column(Float)
    OSP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    OSP_open = Column(Float)
    OSP_high = Column(Float)
    OSP_low = Column(Float)
    OSP_close = Column(Float)
    OSP_volume = Column(Integer)
    OSP_ema_short = Column(Float)
    OSP_ema_long = Column(Float)
    OSP_buy_signal = Column(Boolean, unique=False, default=True)
    OSP_sell_signal = Column(Boolean, unique=False, default=True)
    OSP_green_signal = Column(Float)
    OSP_red_signal = Column(Float)
    PTT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTT_open = Column(Float)
    PTT_high = Column(Float)
    PTT_low = Column(Float)
    PTT_close = Column(Float)
    PTT_volume = Column(Integer)
    PTT_ema_short = Column(Float)
    PTT_ema_long = Column(Float)
    PTT_buy_signal = Column(Boolean, unique=False, default=True)
    PTT_sell_signal = Column(Boolean, unique=False, default=True)
    PTT_green_signal = Column(Float)
    PTT_red_signal = Column(Float)
    PTTEP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTTEP_open = Column(Float)
    PTTEP_high = Column(Float)
    PTTEP_low = Column(Float)
    PTTEP_close = Column(Float)
    PTTEP_volume = Column(Integer)
    PTTEP_ema_short = Column(Float)
    PTTEP_ema_long = Column(Float)
    PTTEP_buy_signal = Column(Boolean, unique=False, default=True)
    PTTEP_sell_signal = Column(Boolean, unique=False, default=True)
    PTTEP_green_signal = Column(Float)
    PTTEP_red_signal = Column(Float)
    PTTGC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTTGC_open = Column(Float)
    PTTGC_high = Column(Float)
    PTTGC_low = Column(Float)
    PTTGC_close = Column(Float)
    PTTGC_volume = Column(Integer)
    PTTGC_ema_short = Column(Float)
    PTTGC_ema_long = Column(Float)
    PTTGC_buy_signal = Column(Boolean, unique=False, default=True)
    PTTGC_sell_signal = Column(Boolean, unique=False, default=True)
    PTTGC_green_signal = Column(Float)
    PTTGC_red_signal = Column(Float)
    RATCH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    RATCH_open = Column(Float)
    RATCH_high = Column(Float)
    RATCH_low = Column(Float)
    RATCH_close = Column(Float)
    RATCH_volume = Column(Integer)
    RATCH_ema_short = Column(Float)
    RATCH_ema_long = Column(Float)
    RATCH_buy_signal = Column(Boolean, unique=False, default=True)
    RATCH_sell_signal = Column(Boolean, unique=False, default=True)
    RATCH_green_signal = Column(Float)
    RATCH_red_signal = Column(Float)
    SAWAD_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SAWAD_open = Column(Float)
    SAWAD_high = Column(Float)
    SAWAD_low = Column(Float)
    SAWAD_close = Column(Float)
    SAWAD_volume = Column(Integer)
    SAWAD_ema_short = Column(Float)
    SAWAD_ema_long = Column(Float)
    SAWAD_buy_signal = Column(Boolean, unique=False, default=True)
    SAWAD_sell_signal = Column(Boolean, unique=False, default=True)
    SAWAD_green_signal = Column(Float)
    SAWAD_red_signal = Column(Float)
    SCB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCB_open = Column(Float)
    SCB_high = Column(Float)
    SCB_low = Column(Float)
    SCB_close = Column(Float)
    SCB_volume = Column(Integer)
    SCB_ema_short = Column(Float)
    SCB_ema_long = Column(Float)
    SCB_buy_signal = Column(Boolean, unique=False, default=True)
    SCB_sell_signal = Column(Boolean, unique=False, default=True)
    SCB_green_signal = Column(Float)
    SCB_red_signal = Column(Float)
    SCC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCC_open = Column(Float)
    SCC_high = Column(Float)
    SCC_low = Column(Float)
    SCC_close = Column(Float)
    SCC_volume = Column(Integer)
    SCC_ema_short = Column(Float)
    SCC_ema_long = Column(Float)
    SCC_buy_signal = Column(Boolean, unique=False, default=True)
    SCC_sell_signal = Column(Boolean, unique=False, default=True)
    SCC_green_signal = Column(Float)
    SCC_red_signal = Column(Float)
    SCGP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCGP_open = Column(Float)
    SCGP_high = Column(Float)
    SCGP_low = Column(Float)
    SCGP_close = Column(Float)
    SCGP_volume = Column(Integer)
    SCGP_ema_short = Column(Float)
    SCGP_ema_long = Column(Float)
    SCGP_buy_signal = Column(Boolean, unique=False, default=True)
    SCGP_sell_signal = Column(Boolean, unique=False, default=True)
    SCGP_green_signal = Column(Float)
    SCGP_red_signal = Column(Float)
    TISCO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TISCO_open = Column(Float)
    TISCO_high = Column(Float)
    TISCO_low = Column(Float)
    TISCO_close = Column(Float)
    TISCO_volume = Column(Integer)
    TISCO_ema_short = Column(Float)
    TISCO_ema_long = Column(Float)
    TISCO_buy_signal = Column(Boolean, unique=False, default=True)
    TISCO_sell_signal = Column(Boolean, unique=False, default=True)
    TISCO_green_signal = Column(Float)
    TISCO_red_signal = Column(Float)
    TOP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TOP_open = Column(Float)
    TOP_high = Column(Float)
    TOP_low = Column(Float)
    TOP_close = Column(Float)
    TOP_volume = Column(Integer)
    TOP_ema_short = Column(Float)
    TOP_ema_long = Column(Float)
    TOP_buy_signal = Column(Boolean, unique=False, default=True)
    TOP_sell_signal = Column(Boolean, unique=False, default=True)
    TOP_green_signal = Column(Float)
    TOP_red_signal = Column(Float)
    TRUE_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TRUE_open = Column(Float)
    TRUE_high = Column(Float)
    TRUE_low = Column(Float)
    TRUE_close = Column(Float)
    TRUE_volume = Column(Integer)
    TRUE_ema_short = Column(Float)
    TRUE_ema_long = Column(Float)
    TRUE_buy_signal = Column(Boolean, unique=False, default=True)
    TRUE_sell_signal = Column(Boolean, unique=False, default=True)
    TRUE_green_signal = Column(Float)
    TRUE_red_signal = Column(Float)
    TTB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TTB_open = Column(Float)
    TTB_high = Column(Float)
    TTB_low = Column(Float)
    TTB_close = Column(Float)
    TTB_volume = Column(Integer)
    TTB_ema_short = Column(Float)
    TTB_ema_long = Column(Float)
    TTB_buy_signal = Column(Boolean, unique=False, default=True)
    TTB_sell_signal = Column(Boolean, unique=False, default=True)
    TTB_green_signal = Column(Float)
    TTB_red_signal = Column(Float)
    TU_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TU_open = Column(Float)
    TU_high = Column(Float)
    TU_low = Column(Float)
    TU_close = Column(Float)
    TU_volume = Column(Integer)
    TU_ema_short = Column(Float)
    TU_ema_long = Column(Float)
    TU_buy_signal = Column(Boolean, unique=False, default=True)
    TU_sell_signal = Column(Boolean, unique=False, default=True)
    TU_green_signal = Column(Float)
    TU_red_signal = Column(Float)
    WHA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    WHA_open = Column(Float)
    WHA_high = Column(Float)
    WHA_low = Column(Float)
    WHA_close = Column(Float)
    WHA_volume = Column(Integer)
    WHA_ema_short = Column(Float)
    WHA_ema_long = Column(Float)
    WHA_buy_signal = Column(Boolean, unique=False, default=True)
    WHA_sell_signal = Column(Boolean, unique=False, default=True)
    WHA_green_signal = Column(Float)
    WHA_red_signal = Column(Float)


class BacktestStrategyRSI():
    ADVANC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    ADVANC_open = Column(Float)
    ADVANC_high = Column(Float)
    ADVANC_low = Column(Float)
    ADVANC_close = Column(Float)
    ADVANC_volume = Column(Integer)
    ADVANC_rsi = Column(Float)
    ADVANC_buy_signal = Column(Boolean, unique=False, default=True)
    ADVANC_sell_signal = Column(Boolean, unique=False, default=True)
    ADVANC_green_signal = Column(Float)
    ADVANC_red_signal = Column(Float)
    AOT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    AOT_open = Column(Float)
    AOT_high = Column(Float)
    AOT_low = Column(Float)
    AOT_close = Column(Float)
    AOT_volume = Column(Integer)
    AOT_rsi = Column(Float)
    AOT_buy_signal = Column(Boolean, unique=False, default=True)
    AOT_sell_signal = Column(Boolean, unique=False, default=True)
    AOT_green_signal = Column(Float)
    AOT_red_signal = Column(Float)
    AWC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    AWC_open = Column(Float)
    AWC_high = Column(Float)
    AWC_low = Column(Float)
    AWC_close = Column(Float)
    AWC_volume = Column(Integer)
    AWC_rsi = Column(Float)
    AWC_buy_signal = Column(Boolean, unique=False, default=True)
    AWC_sell_signal = Column(Boolean, unique=False, default=True)
    AWC_green_signal = Column(Float)
    AWC_red_signal = Column(Float)
    BANPU_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BANPU_open = Column(Float)
    BANPU_high = Column(Float)
    BANPU_low = Column(Float)
    BANPU_close = Column(Float)
    BANPU_volume = Column(Integer)
    BANPU_rsi = Column(Float)
    BANPU_buy_signal = Column(Boolean, unique=False, default=True)
    BANPU_sell_signal = Column(Boolean, unique=False, default=True)
    BANPU_green_signal = Column(Float)
    BANPU_red_signal = Column(Float)
    BBL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BBL_open = Column(Float)
    BBL_high = Column(Float)
    BBL_low = Column(Float)
    BBL_close = Column(Float)
    BBL_volume = Column(Integer)
    BBL_rsi = Column(Float)
    BBL_buy_signal = Column(Boolean, unique=False, default=True)
    BBL_sell_signal = Column(Boolean, unique=False, default=True)
    BBL_green_signal = Column(Float)
    BBL_red_signal = Column(Float)
    BDMS_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BDMS_open = Column(Float)
    BDMS_high = Column(Float)
    BDMS_low = Column(Float)
    BDMS_close = Column(Float)
    BDMS_volume = Column(Integer)
    BDMS_rsi = Column(Float)
    BDMS_buy_signal = Column(Boolean, unique=False, default=True)
    BDMS_sell_signal = Column(Boolean, unique=False, default=True)
    BDMS_green_signal = Column(Float)
    BDMS_red_signal = Column(Float)
    BEM_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BEM_open = Column(Float)
    BEM_high = Column(Float)
    BEM_low = Column(Float)
    BEM_close = Column(Float)
    BEM_volume = Column(Integer)
    BEM_rsi = Column(Float)
    BEM_buy_signal = Column(Boolean, unique=False, default=True)
    BEM_sell_signal = Column(Boolean, unique=False, default=True)
    BEM_green_signal = Column(Float)
    BEM_red_signal = Column(Float)
    BGRIM_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BGRIM_open = Column(Float)
    BGRIM_high = Column(Float)
    BGRIM_low = Column(Float)
    BGRIM_close = Column(Float)
    BGRIM_volume = Column(Integer)
    BGRIM_rsi = Column(Float)
    BGRIM_buy_signal = Column(Boolean, unique=False, default=True)
    BGRIM_sell_signal = Column(Boolean, unique=False, default=True)
    BGRIM_green_signal = Column(Float)
    BGRIM_red_signal = Column(Float)
    BH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BH_open = Column(Float)
    BH_high = Column(Float)
    BH_low = Column(Float)
    BH_close = Column(Float)
    BH_volume = Column(Integer)
    BH_rsi = Column(Float)
    BH_buy_signal = Column(Boolean, unique=False, default=True)
    BH_sell_signal = Column(Boolean, unique=False, default=True)
    BH_green_signal = Column(Float)
    BH_red_signal = Column(Float)
    BTS_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BTS_open = Column(Float)
    BTS_high = Column(Float)
    BTS_low = Column(Float)
    BTS_close = Column(Float)
    BTS_volume = Column(Integer)
    BTS_rsi = Column(Float)
    BTS_buy_signal = Column(Boolean, unique=False, default=True)
    BTS_sell_signal = Column(Boolean, unique=False, default=True)
    BTS_green_signal = Column(Float)
    BTS_red_signal = Column(Float)
    CBG_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CBG_open = Column(Float)
    CBG_high = Column(Float)
    CBG_low = Column(Float)
    CBG_close = Column(Float)
    CBG_volume = Column(Integer)
    CBG_rsi = Column(Float)
    CBG_buy_signal = Column(Boolean, unique=False, default=True)
    CBG_sell_signal = Column(Boolean, unique=False, default=True)
    CBG_green_signal = Column(Float)
    CBG_red_signal = Column(Float)
    CENTEL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CENTEL_open = Column(Float)
    CENTEL_high = Column(Float)
    CENTEL_low = Column(Float)
    CENTEL_close = Column(Float)
    CENTEL_volume = Column(Integer)
    CENTEL_rsi = Column(Float)
    CENTEL_buy_signal = Column(Boolean, unique=False, default=True)
    CENTEL_sell_signal = Column(Boolean, unique=False, default=True)
    CENTEL_green_signal = Column(Float)
    CENTEL_red_signal = Column(Float)
    COM7_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    COM7_open = Column(Float)
    COM7_high = Column(Float)
    COM7_low = Column(Float)
    COM7_close = Column(Float)
    COM7_volume = Column(Integer)
    COM7_rsi = Column(Float)
    COM7_buy_signal = Column(Boolean, unique=False, default=True)
    COM7_sell_signal = Column(Boolean, unique=False, default=True)
    COM7_green_signal = Column(Float)
    COM7_red_signal = Column(Float)
    CPALL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPALL_open = Column(Float)
    CPALL_high = Column(Float)
    CPALL_low = Column(Float)
    CPALL_close = Column(Float)
    CPALL_volume = Column(Integer)
    CPALL_rsi = Column(Float)
    CPALL_buy_signal = Column(Boolean, unique=False, default=True)
    CPALL_sell_signal = Column(Boolean, unique=False, default=True)
    CPALL_green_signal = Column(Float)
    CPALL_red_signal = Column(Float)
    CPF_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPF_open = Column(Float)
    CPF_high = Column(Float)
    CPF_low = Column(Float)
    CPF_close = Column(Float)
    CPF_volume = Column(Integer)
    CPF_rsi = Column(Float)
    CPF_buy_signal = Column(Boolean, unique=False, default=True)
    CPF_sell_signal = Column(Boolean, unique=False, default=True)
    CPF_green_signal = Column(Float)
    CPF_red_signal = Column(Float)
    CPN_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPN_open = Column(Float)
    CPN_high = Column(Float)
    CPN_low = Column(Float)
    CPN_close = Column(Float)
    CPN_volume = Column(Integer)
    CPN_rsi = Column(Float)
    CPN_buy_signal = Column(Boolean, unique=False, default=True)
    CPN_sell_signal = Column(Boolean, unique=False, default=True)
    CPN_green_signal = Column(Float)
    CPN_red_signal = Column(Float)
    CRC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CRC_open = Column(Float)
    CRC_high = Column(Float)
    CRC_low = Column(Float)
    CRC_close = Column(Float)
    CRC_volume = Column(Integer)
    CRC_rsi = Column(Float)
    CRC_buy_signal = Column(Boolean, unique=False, default=True)
    CRC_sell_signal = Column(Boolean, unique=False, default=True)
    CRC_green_signal = Column(Float)
    CRC_red_signal = Column(Float)
    DELTA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    DELTA_open = Column(Float)
    DELTA_high = Column(Float)
    DELTA_low = Column(Float)
    DELTA_close = Column(Float)
    DELTA_volume = Column(Integer)
    DELTA_rsi = Column(Float)
    DELTA_buy_signal = Column(Boolean, unique=False, default=True)
    DELTA_sell_signal = Column(Boolean, unique=False, default=True)
    DELTA_green_signal = Column(Float)
    DELTA_red_signal = Column(Float)
    EA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    EA_open = Column(Float)
    EA_high = Column(Float)
    EA_low = Column(Float)
    EA_close = Column(Float)
    EA_volume = Column(Integer)
    EA_rsi = Column(Float)
    EA_buy_signal = Column(Boolean, unique=False, default=True)
    EA_sell_signal = Column(Boolean, unique=False, default=True)
    EA_green_signal = Column(Float)
    EA_red_signal = Column(Float)
    EGCO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    EGCO_open = Column(Float)
    EGCO_high = Column(Float)
    EGCO_low = Column(Float)
    EGCO_close = Column(Float)
    EGCO_volume = Column(Integer)
    EGCO_rsi = Column(Float)
    EGCO_buy_signal = Column(Boolean, unique=False, default=True)
    EGCO_sell_signal = Column(Boolean, unique=False, default=True)
    EGCO_green_signal = Column(Float)
    EGCO_red_signal = Column(Float)
    GLOBAL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GLOBAL_open = Column(Float)
    GLOBAL_high = Column(Float)
    GLOBAL_low = Column(Float)
    GLOBAL_close = Column(Float)
    GLOBAL_volume = Column(Integer)
    GLOBAL_rsi = Column(Float)
    GLOBAL_buy_signal = Column(Boolean, unique=False, default=True)
    GLOBAL_sell_signal = Column(Boolean, unique=False, default=True)
    GLOBAL_green_signal = Column(Float)
    GLOBAL_red_signal = Column(Float)
    GPSC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GPSC_open = Column(Float)
    GPSC_high = Column(Float)
    GPSC_low = Column(Float)
    GPSC_close = Column(Float)
    GPSC_volume = Column(Integer)
    GPSC_rsi = Column(Float)
    GPSC_buy_signal = Column(Boolean, unique=False, default=True)
    GPSC_sell_signal = Column(Boolean, unique=False, default=True)
    GPSC_green_signal = Column(Float)
    GPSC_red_signal = Column(Float)
    GULF_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GULF_open = Column(Float)
    GULF_high = Column(Float)
    GULF_low = Column(Float)
    GULF_close = Column(Float)
    GULF_volume = Column(Integer)
    GULF_rsi = Column(Float)
    GULF_buy_signal = Column(Boolean, unique=False, default=True)
    GULF_sell_signal = Column(Boolean, unique=False, default=True)
    GULF_green_signal = Column(Float)
    GULF_red_signal = Column(Float)
    HMPRO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    HMPRO_open = Column(Float)
    HMPRO_high = Column(Float)
    HMPRO_low = Column(Float)
    HMPRO_close = Column(Float)
    HMPRO_volume = Column(Integer)
    HMPRO_rsi = Column(Float)
    HMPRO_buy_signal = Column(Boolean, unique=False, default=True)
    HMPRO_sell_signal = Column(Boolean, unique=False, default=True)
    HMPRO_green_signal = Column(Float)
    HMPRO_red_signal = Column(Float)
    INTUCH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    INTUCH_open = Column(Float)
    INTUCH_high = Column(Float)
    INTUCH_low = Column(Float)
    INTUCH_close = Column(Float)
    INTUCH_volume = Column(Integer)
    INTUCH_rsi = Column(Float)
    INTUCH_buy_signal = Column(Boolean, unique=False, default=True)
    INTUCH_sell_signal = Column(Boolean, unique=False, default=True)
    INTUCH_green_signal = Column(Float)
    INTUCH_red_signal = Column(Float)
    IVL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    IVL_open = Column(Float)
    IVL_high = Column(Float)
    IVL_low = Column(Float)
    IVL_close = Column(Float)
    IVL_volume = Column(Integer)
    IVL_rsi = Column(Float)
    IVL_buy_signal = Column(Boolean, unique=False, default=True)
    IVL_sell_signal = Column(Boolean, unique=False, default=True)
    IVL_green_signal = Column(Float)
    IVL_red_signal = Column(Float)
    KBANK_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KBANK_open = Column(Float)
    KBANK_high = Column(Float)
    KBANK_low = Column(Float)
    KBANK_close = Column(Float)
    KBANK_volume = Column(Integer)
    KBANK_rsi = Column(Float)
    KBANK_buy_signal = Column(Boolean, unique=False, default=True)
    KBANK_sell_signal = Column(Boolean, unique=False, default=True)
    KBANK_green_signal = Column(Float)
    KBANK_red_signal = Column(Float)
    KCE_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KCE_open = Column(Float)
    KCE_high = Column(Float)
    KCE_low = Column(Float)
    KCE_close = Column(Float)
    KCE_volume = Column(Integer)
    KCE_rsi = Column(Float)
    KCE_buy_signal = Column(Boolean, unique=False, default=True)
    KCE_sell_signal = Column(Boolean, unique=False, default=True)
    KCE_green_signal = Column(Float)
    KCE_red_signal = Column(Float)
    KTB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KTB_open = Column(Float)
    KTB_high = Column(Float)
    KTB_low = Column(Float)
    KTB_close = Column(Float)
    KTB_volume = Column(Integer)
    KTB_rsi = Column(Float)
    KTB_buy_signal = Column(Boolean, unique=False, default=True)
    KTB_sell_signal = Column(Boolean, unique=False, default=True)
    KTB_green_signal = Column(Float)
    KTB_red_signal = Column(Float)
    KTC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KTC_open = Column(Float)
    KTC_high = Column(Float)
    KTC_low = Column(Float)
    KTC_close = Column(Float)
    KTC_volume = Column(Integer)
    KTC_rsi = Column(Float)
    KTC_buy_signal = Column(Boolean, unique=False, default=True)
    KTC_sell_signal = Column(Boolean, unique=False, default=True)
    KTC_green_signal = Column(Float)
    KTC_red_signal = Column(Float)
    LH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    LH_open = Column(Float)
    LH_high = Column(Float)
    LH_low = Column(Float)
    LH_close = Column(Float)
    LH_volume = Column(Integer)
    LH_rsi = Column(Float)
    LH_buy_signal = Column(Boolean, unique=False, default=True)
    LH_sell_signal = Column(Boolean, unique=False, default=True)
    LH_green_signal = Column(Float)
    LH_red_signal = Column(Float)
    MINT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    MINT_open = Column(Float)
    MINT_high = Column(Float)
    MINT_low = Column(Float)
    MINT_close = Column(Float)
    MINT_volume = Column(Integer)
    MINT_rsi = Column(Float)
    MINT_buy_signal = Column(Boolean, unique=False, default=True)
    MINT_sell_signal = Column(Boolean, unique=False, default=True)
    MINT_green_signal = Column(Float)
    MINT_red_signal = Column(Float)
    MTC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    MTC_open = Column(Float)
    MTC_high = Column(Float)
    MTC_low = Column(Float)
    MTC_close = Column(Float)
    MTC_volume = Column(Integer)
    MTC_rsi = Column(Float)
    MTC_buy_signal = Column(Boolean, unique=False, default=True)
    MTC_sell_signal = Column(Boolean, unique=False, default=True)
    MTC_green_signal = Column(Float)
    MTC_red_signal = Column(Float)
    OR_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    OR_open = Column(Float)
    OR_high = Column(Float)
    OR_low = Column(Float)
    OR_close = Column(Float)
    OR_volume = Column(Integer)
    OR_rsi = Column(Float)
    OR_buy_signal = Column(Boolean, unique=False, default=True)
    OR_sell_signal = Column(Boolean, unique=False, default=True)
    OR_green_signal = Column(Float)
    OR_red_signal = Column(Float)
    OSP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    OSP_open = Column(Float)
    OSP_high = Column(Float)
    OSP_low = Column(Float)
    OSP_close = Column(Float)
    OSP_volume = Column(Integer)
    OSP_rsi = Column(Float)
    OSP_buy_signal = Column(Boolean, unique=False, default=True)
    OSP_sell_signal = Column(Boolean, unique=False, default=True)
    OSP_green_signal = Column(Float)
    OSP_red_signal = Column(Float)
    PTT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTT_open = Column(Float)
    PTT_high = Column(Float)
    PTT_low = Column(Float)
    PTT_close = Column(Float)
    PTT_volume = Column(Integer)
    PTT_rsi = Column(Float)
    PTT_buy_signal = Column(Boolean, unique=False, default=True)
    PTT_sell_signal = Column(Boolean, unique=False, default=True)
    PTT_green_signal = Column(Float)
    PTT_red_signal = Column(Float)
    PTTEP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTTEP_open = Column(Float)
    PTTEP_high = Column(Float)
    PTTEP_low = Column(Float)
    PTTEP_close = Column(Float)
    PTTEP_volume = Column(Integer)
    PTTEP_rsi = Column(Float)
    PTTEP_buy_signal = Column(Boolean, unique=False, default=True)
    PTTEP_sell_signal = Column(Boolean, unique=False, default=True)
    PTTEP_green_signal = Column(Float)
    PTTEP_red_signal = Column(Float)
    PTTGC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTTGC_open = Column(Float)
    PTTGC_high = Column(Float)
    PTTGC_low = Column(Float)
    PTTGC_close = Column(Float)
    PTTGC_volume = Column(Integer)
    PTTGC_rsi = Column(Float)
    PTTGC_buy_signal = Column(Boolean, unique=False, default=True)
    PTTGC_sell_signal = Column(Boolean, unique=False, default=True)
    PTTGC_green_signal = Column(Float)
    PTTGC_red_signal = Column(Float)
    RATCH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    RATCH_open = Column(Float)
    RATCH_high = Column(Float)
    RATCH_low = Column(Float)
    RATCH_close = Column(Float)
    RATCH_volume = Column(Integer)
    RATCH_rsi = Column(Float)
    RATCH_buy_signal = Column(Boolean, unique=False, default=True)
    RATCH_sell_signal = Column(Boolean, unique=False, default=True)
    RATCH_green_signal = Column(Float)
    RATCH_red_signal = Column(Float)
    SAWAD_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SAWAD_open = Column(Float)
    SAWAD_high = Column(Float)
    SAWAD_low = Column(Float)
    SAWAD_close = Column(Float)
    SAWAD_volume = Column(Integer)
    SAWAD_rsi = Column(Float)
    SAWAD_buy_signal = Column(Boolean, unique=False, default=True)
    SAWAD_sell_signal = Column(Boolean, unique=False, default=True)
    SAWAD_green_signal = Column(Float)
    SAWAD_red_signal = Column(Float)
    SCB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCB_open = Column(Float)
    SCB_high = Column(Float)
    SCB_low = Column(Float)
    SCB_close = Column(Float)
    SCB_volume = Column(Integer)
    SCB_rsi = Column(Float)
    SCB_buy_signal = Column(Boolean, unique=False, default=True)
    SCB_sell_signal = Column(Boolean, unique=False, default=True)
    SCB_green_signal = Column(Float)
    SCB_red_signal = Column(Float)
    SCC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCC_open = Column(Float)
    SCC_high = Column(Float)
    SCC_low = Column(Float)
    SCC_close = Column(Float)
    SCC_volume = Column(Integer)
    SCC_rsi = Column(Float)
    SCC_buy_signal = Column(Boolean, unique=False, default=True)
    SCC_sell_signal = Column(Boolean, unique=False, default=True)
    SCC_green_signal = Column(Float)
    SCC_red_signal = Column(Float)
    SCGP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCGP_open = Column(Float)
    SCGP_high = Column(Float)
    SCGP_low = Column(Float)
    SCGP_close = Column(Float)
    SCGP_volume = Column(Integer)
    SCGP_rsi = Column(Float)
    SCGP_buy_signal = Column(Boolean, unique=False, default=True)
    SCGP_sell_signal = Column(Boolean, unique=False, default=True)
    SCGP_green_signal = Column(Float)
    SCGP_red_signal = Column(Float)
    TISCO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TISCO_open = Column(Float)
    TISCO_high = Column(Float)
    TISCO_low = Column(Float)
    TISCO_close = Column(Float)
    TISCO_volume = Column(Integer)
    TISCO_rsi = Column(Float)
    TISCO_buy_signal = Column(Boolean, unique=False, default=True)
    TISCO_sell_signal = Column(Boolean, unique=False, default=True)
    TISCO_green_signal = Column(Float)
    TISCO_red_signal = Column(Float)
    TOP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TOP_open = Column(Float)
    TOP_high = Column(Float)
    TOP_low = Column(Float)
    TOP_close = Column(Float)
    TOP_volume = Column(Integer)
    TOP_rsi = Column(Float)
    TOP_buy_signal = Column(Boolean, unique=False, default=True)
    TOP_sell_signal = Column(Boolean, unique=False, default=True)
    TOP_green_signal = Column(Float)
    TOP_red_signal = Column(Float)
    TRUE_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TRUE_open = Column(Float)
    TRUE_high = Column(Float)
    TRUE_low = Column(Float)
    TRUE_close = Column(Float)
    TRUE_volume = Column(Integer)
    TRUE_rsi = Column(Float)
    TRUE_buy_signal = Column(Boolean, unique=False, default=True)
    TRUE_sell_signal = Column(Boolean, unique=False, default=True)
    TRUE_green_signal = Column(Float)
    TRUE_red_signal = Column(Float)
    TTB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TTB_open = Column(Float)
    TTB_high = Column(Float)
    TTB_low = Column(Float)
    TTB_close = Column(Float)
    TTB_volume = Column(Integer)
    TTB_rsi = Column(Float)
    TTB_buy_signal = Column(Boolean, unique=False, default=True)
    TTB_sell_signal = Column(Boolean, unique=False, default=True)
    TTB_green_signal = Column(Float)
    TTB_red_signal = Column(Float)
    TU_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TU_open = Column(Float)
    TU_high = Column(Float)
    TU_low = Column(Float)
    TU_close = Column(Float)
    TU_volume = Column(Integer)
    TU_rsi = Column(Float)
    TU_buy_signal = Column(Boolean, unique=False, default=True)
    TU_sell_signal = Column(Boolean, unique=False, default=True)
    TU_green_signal = Column(Float)
    TU_red_signal = Column(Float)
    WHA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    WHA_open = Column(Float)
    WHA_high = Column(Float)
    WHA_low = Column(Float)
    WHA_close = Column(Float)
    WHA_volume = Column(Integer)
    WHA_rsi = Column(Float)
    WHA_buy_signal = Column(Boolean, unique=False, default=True)
    WHA_sell_signal = Column(Boolean, unique=False, default=True)
    WHA_green_signal = Column(Float)
    WHA_red_signal = Column(Float)


class BacktestStrategyMACD():
    ADVANC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    ADVANC_open = Column(Float)
    ADVANC_high = Column(Float)
    ADVANC_low = Column(Float)
    ADVANC_close = Column(Float)
    ADVANC_volume = Column(Integer)
    ADVANC_macd = Column(Float)
    ADVANC_macds = Column(Float)
    ADVANC_buy_signal = Column(Boolean, unique=False, default=True)
    ADVANC_sell_signal = Column(Boolean, unique=False, default=True)
    ADVANC_green_signal = Column(Float)
    ADVANC_red_signal = Column(Float)
    AOT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    AOT_open = Column(Float)
    AOT_high = Column(Float)
    AOT_low = Column(Float)
    AOT_close = Column(Float)
    AOT_volume = Column(Integer)
    AOT_macd = Column(Float)
    AOT_macds = Column(Float)
    AOT_buy_signal = Column(Boolean, unique=False, default=True)
    AOT_sell_signal = Column(Boolean, unique=False, default=True)
    AOT_green_signal = Column(Float)
    AOT_red_signal = Column(Float)
    AWC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    AWC_open = Column(Float)
    AWC_high = Column(Float)
    AWC_low = Column(Float)
    AWC_close = Column(Float)
    AWC_volume = Column(Integer)
    AWC_macd = Column(Float)
    AWC_macds = Column(Float)
    AWC_buy_signal = Column(Boolean, unique=False, default=True)
    AWC_sell_signal = Column(Boolean, unique=False, default=True)
    AWC_green_signal = Column(Float)
    AWC_red_signal = Column(Float)
    BANPU_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BANPU_open = Column(Float)
    BANPU_high = Column(Float)
    BANPU_low = Column(Float)
    BANPU_close = Column(Float)
    BANPU_volume = Column(Integer)
    BANPU_macd = Column(Float)
    BANPU_macds = Column(Float)
    BANPU_buy_signal = Column(Boolean, unique=False, default=True)
    BANPU_sell_signal = Column(Boolean, unique=False, default=True)
    BANPU_green_signal = Column(Float)
    BANPU_red_signal = Column(Float)
    BBL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BBL_open = Column(Float)
    BBL_high = Column(Float)
    BBL_low = Column(Float)
    BBL_close = Column(Float)
    BBL_volume = Column(Integer)
    BBL_macd = Column(Float)
    BBL_macds = Column(Float)
    BBL_buy_signal = Column(Boolean, unique=False, default=True)
    BBL_sell_signal = Column(Boolean, unique=False, default=True)
    BBL_green_signal = Column(Float)
    BBL_red_signal = Column(Float)
    BDMS_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BDMS_open = Column(Float)
    BDMS_high = Column(Float)
    BDMS_low = Column(Float)
    BDMS_close = Column(Float)
    BDMS_volume = Column(Integer)
    BDMS_macd = Column(Float)
    BDMS_macds = Column(Float)
    BDMS_buy_signal = Column(Boolean, unique=False, default=True)
    BDMS_sell_signal = Column(Boolean, unique=False, default=True)
    BDMS_green_signal = Column(Float)
    BDMS_red_signal = Column(Float)
    BEM_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BEM_open = Column(Float)
    BEM_high = Column(Float)
    BEM_low = Column(Float)
    BEM_close = Column(Float)
    BEM_volume = Column(Integer)
    BEM_macd = Column(Float)
    BEM_macds = Column(Float)
    BEM_buy_signal = Column(Boolean, unique=False, default=True)
    BEM_sell_signal = Column(Boolean, unique=False, default=True)
    BEM_green_signal = Column(Float)
    BEM_red_signal = Column(Float)
    BGRIM_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BGRIM_open = Column(Float)
    BGRIM_high = Column(Float)
    BGRIM_low = Column(Float)
    BGRIM_close = Column(Float)
    BGRIM_volume = Column(Integer)
    BGRIM_macd = Column(Float)
    BGRIM_macds = Column(Float)
    BGRIM_buy_signal = Column(Boolean, unique=False, default=True)
    BGRIM_sell_signal = Column(Boolean, unique=False, default=True)
    BGRIM_green_signal = Column(Float)
    BGRIM_red_signal = Column(Float)
    BH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BH_open = Column(Float)
    BH_high = Column(Float)
    BH_low = Column(Float)
    BH_close = Column(Float)
    BH_volume = Column(Integer)
    BH_macd = Column(Float)
    BH_macds = Column(Float)
    BH_buy_signal = Column(Boolean, unique=False, default=True)
    BH_sell_signal = Column(Boolean, unique=False, default=True)
    BH_green_signal = Column(Float)
    BH_red_signal = Column(Float)
    BTS_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BTS_open = Column(Float)
    BTS_high = Column(Float)
    BTS_low = Column(Float)
    BTS_close = Column(Float)
    BTS_volume = Column(Integer)
    BTS_macd = Column(Float)
    BTS_macds = Column(Float)
    BTS_buy_signal = Column(Boolean, unique=False, default=True)
    BTS_sell_signal = Column(Boolean, unique=False, default=True)
    BTS_green_signal = Column(Float)
    BTS_red_signal = Column(Float)
    CBG_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CBG_open = Column(Float)
    CBG_high = Column(Float)
    CBG_low = Column(Float)
    CBG_close = Column(Float)
    CBG_volume = Column(Integer)
    CBG_macd = Column(Float)
    CBG_macds = Column(Float)
    CBG_buy_signal = Column(Boolean, unique=False, default=True)
    CBG_sell_signal = Column(Boolean, unique=False, default=True)
    CBG_green_signal = Column(Float)
    CBG_red_signal = Column(Float)
    CENTEL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CENTEL_open = Column(Float)
    CENTEL_high = Column(Float)
    CENTEL_low = Column(Float)
    CENTEL_close = Column(Float)
    CENTEL_volume = Column(Integer)
    CENTEL_macd = Column(Float)
    CENTEL_macds = Column(Float)
    CENTEL_buy_signal = Column(Boolean, unique=False, default=True)
    CENTEL_sell_signal = Column(Boolean, unique=False, default=True)
    CENTEL_green_signal = Column(Float)
    CENTEL_red_signal = Column(Float)
    COM7_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    COM7_open = Column(Float)
    COM7_high = Column(Float)
    COM7_low = Column(Float)
    COM7_close = Column(Float)
    COM7_volume = Column(Integer)
    COM7_macd = Column(Float)
    COM7_macds = Column(Float)
    COM7_buy_signal = Column(Boolean, unique=False, default=True)
    COM7_sell_signal = Column(Boolean, unique=False, default=True)
    COM7_green_signal = Column(Float)
    COM7_red_signal = Column(Float)
    CPALL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPALL_open = Column(Float)
    CPALL_high = Column(Float)
    CPALL_low = Column(Float)
    CPALL_close = Column(Float)
    CPALL_volume = Column(Integer)
    CPALL_macd = Column(Float)
    CPALL_macds = Column(Float)
    CPALL_buy_signal = Column(Boolean, unique=False, default=True)
    CPALL_sell_signal = Column(Boolean, unique=False, default=True)
    CPALL_green_signal = Column(Float)
    CPALL_red_signal = Column(Float)
    CPF_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPF_open = Column(Float)
    CPF_high = Column(Float)
    CPF_low = Column(Float)
    CPF_close = Column(Float)
    CPF_volume = Column(Integer)
    CPF_macd = Column(Float)
    CPF_macds = Column(Float)
    CPF_buy_signal = Column(Boolean, unique=False, default=True)
    CPF_sell_signal = Column(Boolean, unique=False, default=True)
    CPF_green_signal = Column(Float)
    CPF_red_signal = Column(Float)
    CPN_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPN_open = Column(Float)
    CPN_high = Column(Float)
    CPN_low = Column(Float)
    CPN_close = Column(Float)
    CPN_volume = Column(Integer)
    CPN_macd = Column(Float)
    CPN_macds = Column(Float)
    CPN_buy_signal = Column(Boolean, unique=False, default=True)
    CPN_sell_signal = Column(Boolean, unique=False, default=True)
    CPN_green_signal = Column(Float)
    CPN_red_signal = Column(Float)
    CRC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CRC_open = Column(Float)
    CRC_high = Column(Float)
    CRC_low = Column(Float)
    CRC_close = Column(Float)
    CRC_volume = Column(Integer)
    CRC_macd = Column(Float)
    CRC_macds = Column(Float)
    CRC_buy_signal = Column(Boolean, unique=False, default=True)
    CRC_sell_signal = Column(Boolean, unique=False, default=True)
    CRC_green_signal = Column(Float)
    CRC_red_signal = Column(Float)
    DELTA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    DELTA_open = Column(Float)
    DELTA_high = Column(Float)
    DELTA_low = Column(Float)
    DELTA_close = Column(Float)
    DELTA_volume = Column(Integer)
    DELTA_macd = Column(Float)
    DELTA_macds = Column(Float)
    DELTA_buy_signal = Column(Boolean, unique=False, default=True)
    DELTA_sell_signal = Column(Boolean, unique=False, default=True)
    DELTA_green_signal = Column(Float)
    DELTA_red_signal = Column(Float)
    EA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    EA_open = Column(Float)
    EA_high = Column(Float)
    EA_low = Column(Float)
    EA_close = Column(Float)
    EA_volume = Column(Integer)
    EA_macd = Column(Float)
    EA_macds = Column(Float)
    EA_buy_signal = Column(Boolean, unique=False, default=True)
    EA_sell_signal = Column(Boolean, unique=False, default=True)
    EA_green_signal = Column(Float)
    EA_red_signal = Column(Float)
    EGCO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    EGCO_open = Column(Float)
    EGCO_high = Column(Float)
    EGCO_low = Column(Float)
    EGCO_close = Column(Float)
    EGCO_volume = Column(Integer)
    EGCO_macd = Column(Float)
    EGCO_macds = Column(Float)
    EGCO_buy_signal = Column(Boolean, unique=False, default=True)
    EGCO_sell_signal = Column(Boolean, unique=False, default=True)
    EGCO_green_signal = Column(Float)
    EGCO_red_signal = Column(Float)
    GLOBAL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GLOBAL_open = Column(Float)
    GLOBAL_high = Column(Float)
    GLOBAL_low = Column(Float)
    GLOBAL_close = Column(Float)
    GLOBAL_volume = Column(Integer)
    GLOBAL_macd = Column(Float)
    GLOBAL_macds = Column(Float)
    GLOBAL_buy_signal = Column(Boolean, unique=False, default=True)
    GLOBAL_sell_signal = Column(Boolean, unique=False, default=True)
    GLOBAL_green_signal = Column(Float)
    GLOBAL_red_signal = Column(Float)
    GPSC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GPSC_open = Column(Float)
    GPSC_high = Column(Float)
    GPSC_low = Column(Float)
    GPSC_close = Column(Float)
    GPSC_volume = Column(Integer)
    GPSC_macd = Column(Float)
    GPSC_macds = Column(Float)
    GPSC_buy_signal = Column(Boolean, unique=False, default=True)
    GPSC_sell_signal = Column(Boolean, unique=False, default=True)
    GPSC_green_signal = Column(Float)
    GPSC_red_signal = Column(Float)
    GULF_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GULF_open = Column(Float)
    GULF_high = Column(Float)
    GULF_low = Column(Float)
    GULF_close = Column(Float)
    GULF_volume = Column(Integer)
    GULF_macd = Column(Float)
    GULF_macds = Column(Float)
    GULF_buy_signal = Column(Boolean, unique=False, default=True)
    GULF_sell_signal = Column(Boolean, unique=False, default=True)
    GULF_green_signal = Column(Float)
    GULF_red_signal = Column(Float)
    HMPRO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    HMPRO_open = Column(Float)
    HMPRO_high = Column(Float)
    HMPRO_low = Column(Float)
    HMPRO_close = Column(Float)
    HMPRO_volume = Column(Integer)
    HMPRO_macd = Column(Float)
    HMPRO_macds = Column(Float)
    HMPRO_buy_signal = Column(Boolean, unique=False, default=True)
    HMPRO_sell_signal = Column(Boolean, unique=False, default=True)
    HMPRO_green_signal = Column(Float)
    HMPRO_red_signal = Column(Float)
    INTUCH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    INTUCH_open = Column(Float)
    INTUCH_high = Column(Float)
    INTUCH_low = Column(Float)
    INTUCH_close = Column(Float)
    INTUCH_volume = Column(Integer)
    INTUCH_macd = Column(Float)
    INTUCH_macds = Column(Float)
    INTUCH_buy_signal = Column(Boolean, unique=False, default=True)
    INTUCH_sell_signal = Column(Boolean, unique=False, default=True)
    INTUCH_green_signal = Column(Float)
    INTUCH_red_signal = Column(Float)
    IVL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    IVL_open = Column(Float)
    IVL_high = Column(Float)
    IVL_low = Column(Float)
    IVL_close = Column(Float)
    IVL_volume = Column(Integer)
    IVL_macd = Column(Float)
    IVL_macds = Column(Float)
    IVL_buy_signal = Column(Boolean, unique=False, default=True)
    IVL_sell_signal = Column(Boolean, unique=False, default=True)
    IVL_green_signal = Column(Float)
    IVL_red_signal = Column(Float)
    KBANK_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KBANK_open = Column(Float)
    KBANK_high = Column(Float)
    KBANK_low = Column(Float)
    KBANK_close = Column(Float)
    KBANK_volume = Column(Integer)
    KBANK_macd = Column(Float)
    KBANK_macds = Column(Float)
    KBANK_buy_signal = Column(Boolean, unique=False, default=True)
    KBANK_sell_signal = Column(Boolean, unique=False, default=True)
    KBANK_green_signal = Column(Float)
    KBANK_red_signal = Column(Float)
    KCE_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KCE_open = Column(Float)
    KCE_high = Column(Float)
    KCE_low = Column(Float)
    KCE_close = Column(Float)
    KCE_volume = Column(Integer)
    KCE_macd = Column(Float)
    KCE_macds = Column(Float)
    KCE_buy_signal = Column(Boolean, unique=False, default=True)
    KCE_sell_signal = Column(Boolean, unique=False, default=True)
    KCE_green_signal = Column(Float)
    KCE_red_signal = Column(Float)
    KTB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KTB_open = Column(Float)
    KTB_high = Column(Float)
    KTB_low = Column(Float)
    KTB_close = Column(Float)
    KTB_volume = Column(Integer)
    KTB_macd = Column(Float)
    KTB_macds = Column(Float)
    KTB_buy_signal = Column(Boolean, unique=False, default=True)
    KTB_sell_signal = Column(Boolean, unique=False, default=True)
    KTB_green_signal = Column(Float)
    KTB_red_signal = Column(Float)
    KTC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KTC_open = Column(Float)
    KTC_high = Column(Float)
    KTC_low = Column(Float)
    KTC_close = Column(Float)
    KTC_volume = Column(Integer)
    KTC_macd = Column(Float)
    KTC_macds = Column(Float)
    KTC_buy_signal = Column(Boolean, unique=False, default=True)
    KTC_sell_signal = Column(Boolean, unique=False, default=True)
    KTC_green_signal = Column(Float)
    KTC_red_signal = Column(Float)
    LH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    LH_open = Column(Float)
    LH_high = Column(Float)
    LH_low = Column(Float)
    LH_close = Column(Float)
    LH_volume = Column(Integer)
    LH_macd = Column(Float)
    LH_macds = Column(Float)
    LH_buy_signal = Column(Boolean, unique=False, default=True)
    LH_sell_signal = Column(Boolean, unique=False, default=True)
    LH_green_signal = Column(Float)
    LH_red_signal = Column(Float)
    MINT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    MINT_open = Column(Float)
    MINT_high = Column(Float)
    MINT_low = Column(Float)
    MINT_close = Column(Float)
    MINT_volume = Column(Integer)
    MINT_macd = Column(Float)
    MINT_macds = Column(Float)
    MINT_buy_signal = Column(Boolean, unique=False, default=True)
    MINT_sell_signal = Column(Boolean, unique=False, default=True)
    MINT_green_signal = Column(Float)
    MINT_red_signal = Column(Float)
    MTC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    MTC_open = Column(Float)
    MTC_high = Column(Float)
    MTC_low = Column(Float)
    MTC_close = Column(Float)
    MTC_volume = Column(Integer)
    MTC_macd = Column(Float)
    MTC_macds = Column(Float)
    MTC_buy_signal = Column(Boolean, unique=False, default=True)
    MTC_sell_signal = Column(Boolean, unique=False, default=True)
    MTC_green_signal = Column(Float)
    MTC_red_signal = Column(Float)
    OR_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    OR_open = Column(Float)
    OR_high = Column(Float)
    OR_low = Column(Float)
    OR_close = Column(Float)
    OR_volume = Column(Integer)
    OR_macd = Column(Float)
    OR_macds = Column(Float)
    OR_buy_signal = Column(Boolean, unique=False, default=True)
    OR_sell_signal = Column(Boolean, unique=False, default=True)
    OR_green_signal = Column(Float)
    OR_red_signal = Column(Float)
    OSP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    OSP_open = Column(Float)
    OSP_high = Column(Float)
    OSP_low = Column(Float)
    OSP_close = Column(Float)
    OSP_volume = Column(Integer)
    OSP_macd = Column(Float)
    OSP_macds = Column(Float)
    OSP_buy_signal = Column(Boolean, unique=False, default=True)
    OSP_sell_signal = Column(Boolean, unique=False, default=True)
    OSP_green_signal = Column(Float)
    OSP_red_signal = Column(Float)
    PTT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTT_open = Column(Float)
    PTT_high = Column(Float)
    PTT_low = Column(Float)
    PTT_close = Column(Float)
    PTT_volume = Column(Integer)
    PTT_macd = Column(Float)
    PTT_macds = Column(Float)
    PTT_buy_signal = Column(Boolean, unique=False, default=True)
    PTT_sell_signal = Column(Boolean, unique=False, default=True)
    PTT_green_signal = Column(Float)
    PTT_red_signal = Column(Float)
    PTTEP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTTEP_open = Column(Float)
    PTTEP_high = Column(Float)
    PTTEP_low = Column(Float)
    PTTEP_close = Column(Float)
    PTTEP_volume = Column(Integer)
    PTTEP_macd = Column(Float)
    PTTEP_macds = Column(Float)
    PTTEP_buy_signal = Column(Boolean, unique=False, default=True)
    PTTEP_sell_signal = Column(Boolean, unique=False, default=True)
    PTTEP_green_signal = Column(Float)
    PTTEP_red_signal = Column(Float)
    PTTGC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTTGC_open = Column(Float)
    PTTGC_high = Column(Float)
    PTTGC_low = Column(Float)
    PTTGC_close = Column(Float)
    PTTGC_volume = Column(Integer)
    PTTGC_macd = Column(Float)
    PTTGC_macds = Column(Float)
    PTTGC_buy_signal = Column(Boolean, unique=False, default=True)
    PTTGC_sell_signal = Column(Boolean, unique=False, default=True)
    PTTGC_green_signal = Column(Float)
    PTTGC_red_signal = Column(Float)
    RATCH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    RATCH_open = Column(Float)
    RATCH_high = Column(Float)
    RATCH_low = Column(Float)
    RATCH_close = Column(Float)
    RATCH_volume = Column(Integer)
    RATCH_macd = Column(Float)
    RATCH_macds = Column(Float)
    RATCH_buy_signal = Column(Boolean, unique=False, default=True)
    RATCH_sell_signal = Column(Boolean, unique=False, default=True)
    RATCH_green_signal = Column(Float)
    RATCH_red_signal = Column(Float)
    SAWAD_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SAWAD_open = Column(Float)
    SAWAD_high = Column(Float)
    SAWAD_low = Column(Float)
    SAWAD_close = Column(Float)
    SAWAD_volume = Column(Integer)
    SAWAD_macd = Column(Float)
    SAWAD_macds = Column(Float)
    SAWAD_buy_signal = Column(Boolean, unique=False, default=True)
    SAWAD_sell_signal = Column(Boolean, unique=False, default=True)
    SAWAD_green_signal = Column(Float)
    SAWAD_red_signal = Column(Float)
    SCB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCB_open = Column(Float)
    SCB_high = Column(Float)
    SCB_low = Column(Float)
    SCB_close = Column(Float)
    SCB_volume = Column(Integer)
    SCB_macd = Column(Float)
    SCB_macds = Column(Float)
    SCB_buy_signal = Column(Boolean, unique=False, default=True)
    SCB_sell_signal = Column(Boolean, unique=False, default=True)
    SCB_green_signal = Column(Float)
    SCB_red_signal = Column(Float)
    SCC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCC_open = Column(Float)
    SCC_high = Column(Float)
    SCC_low = Column(Float)
    SCC_close = Column(Float)
    SCC_volume = Column(Integer)
    SCC_macd = Column(Float)
    SCC_macds = Column(Float)
    SCC_buy_signal = Column(Boolean, unique=False, default=True)
    SCC_sell_signal = Column(Boolean, unique=False, default=True)
    SCC_green_signal = Column(Float)
    SCC_red_signal = Column(Float)
    SCGP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCGP_open = Column(Float)
    SCGP_high = Column(Float)
    SCGP_low = Column(Float)
    SCGP_close = Column(Float)
    SCGP_volume = Column(Integer)
    SCGP_macd = Column(Float)
    SCGP_macds = Column(Float)
    SCGP_buy_signal = Column(Boolean, unique=False, default=True)
    SCGP_sell_signal = Column(Boolean, unique=False, default=True)
    SCGP_green_signal = Column(Float)
    SCGP_red_signal = Column(Float)
    TISCO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TISCO_open = Column(Float)
    TISCO_high = Column(Float)
    TISCO_low = Column(Float)
    TISCO_close = Column(Float)
    TISCO_volume = Column(Integer)
    TISCO_macd = Column(Float)
    TISCO_macds = Column(Float)
    TISCO_buy_signal = Column(Boolean, unique=False, default=True)
    TISCO_sell_signal = Column(Boolean, unique=False, default=True)
    TISCO_green_signal = Column(Float)
    TISCO_red_signal = Column(Float)
    TOP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TOP_open = Column(Float)
    TOP_high = Column(Float)
    TOP_low = Column(Float)
    TOP_close = Column(Float)
    TOP_volume = Column(Integer)
    TOP_macd = Column(Float)
    TOP_macds = Column(Float)
    TOP_buy_signal = Column(Boolean, unique=False, default=True)
    TOP_sell_signal = Column(Boolean, unique=False, default=True)
    TOP_green_signal = Column(Float)
    TOP_red_signal = Column(Float)
    TRUE_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TRUE_open = Column(Float)
    TRUE_high = Column(Float)
    TRUE_low = Column(Float)
    TRUE_close = Column(Float)
    TRUE_volume = Column(Integer)
    TRUE_macd = Column(Float)
    TRUE_macds = Column(Float)
    TRUE_buy_signal = Column(Boolean, unique=False, default=True)
    TRUE_sell_signal = Column(Boolean, unique=False, default=True)
    TRUE_green_signal = Column(Float)
    TRUE_red_signal = Column(Float)
    TTB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TTB_open = Column(Float)
    TTB_high = Column(Float)
    TTB_low = Column(Float)
    TTB_close = Column(Float)
    TTB_volume = Column(Integer)
    TTB_macd = Column(Float)
    TTB_macds = Column(Float)
    TTB_buy_signal = Column(Boolean, unique=False, default=True)
    TTB_sell_signal = Column(Boolean, unique=False, default=True)
    TTB_green_signal = Column(Float)
    TTB_red_signal = Column(Float)
    TU_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TU_open = Column(Float)
    TU_high = Column(Float)
    TU_low = Column(Float)
    TU_close = Column(Float)
    TU_volume = Column(Integer)
    TU_macd = Column(Float)
    TU_macds = Column(Float)
    TU_buy_signal = Column(Boolean, unique=False, default=True)
    TU_sell_signal = Column(Boolean, unique=False, default=True)
    TU_green_signal = Column(Float)
    TU_red_signal = Column(Float)
    WHA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    WHA_open = Column(Float)
    WHA_high = Column(Float)
    WHA_low = Column(Float)
    WHA_close = Column(Float)
    WHA_volume = Column(Integer)
    WHA_macd = Column(Float)
    WHA_macds = Column(Float)
    WHA_buy_signal = Column(Boolean, unique=False, default=True)
    WHA_sell_signal = Column(Boolean, unique=False, default=True)
    WHA_green_signal = Column(Float)
    WHA_red_signal = Column(Float)


class StatsStrategy():
    index = Column(String)
    ADVANC_stats = Column(Float)
    AOT_stats = Column(Float)
    AWC_stats = Column(Float)
    BANPU_stats = Column(Float)
    BBL_stats = Column(Float)
    BDMS_stats = Column(Float)
    BEM_stats = Column(Float)
    BGRIM_stats = Column(Float)
    BH_stats = Column(Float)
    BTS_stats = Column(Float)
    CBG_stats = Column(Float)
    CENTEL_stats = Column(Float)
    COM7_stats = Column(Float)
    CPALL_stats = Column(Float)
    CPF_stats = Column(Float)
    CPN_stats = Column(Float)
    CRC_stats = Column(Float)
    DELTA_stats = Column(Float)
    EA_stats = Column(Float)
    EGCO_stats = Column(Float)
    GLOBAL_stats = Column(Float)
    GPSC_stats = Column(Float)
    GULF_stats = Column(Float)
    HMPRO_stats = Column(Float)
    INTUCH_stats = Column(Float)
    IVL_stats = Column(Float)
    KBANK_stats = Column(Float)
    KCE_stats = Column(Float)
    KTB_stats = Column(Float)
    KTC_stats = Column(Float)
    LH_stats = Column(Float)
    MINT_stats = Column(Float)
    MTC_stats = Column(Float)
    OR_stats = Column(Float)
    OSP_stats = Column(Float)
    PTT_stats = Column(Float)
    PTTEP_stats = Column(Float)
    PTTGC_stats = Column(Float)
    RATCH_stats = Column(Float)
    SAWAD_stats = Column(Float)
    SCB_stats = Column(Float)
    SCC_stats = Column(Float)
    SCGP_stats = Column(Float)
    TISCO_stats = Column(Float)
    TOP_stats = Column(Float)
    TRUE_stats = Column(Float)
    TTB_stats = Column(Float)
    TU_stats = Column(Float)
    WHA_stats = Column(Float)


class TradeHistory():
    ADVANC_signal_index = Column(String)
    ADVANC_side = Column(String)
    ADVANC_stop_type = Column(String)
    ADVANC_price = Column(Float)
    ADVANC_fees = Column(Float)
    ADVANC_pnl = Column(Float)
    ADVANC_return = Column(Float)
    ADVANC_direction = Column(String)
    ADVANC_status = Column(String)
    AOT_signal_index = Column(String)
    AOT_side = Column(String)
    AOT_stop_type = Column(String)
    AOT_price = Column(Float)
    AOT_fees = Column(Float)
    AOT_pnl = Column(Float)
    AOT_return = Column(Float)
    AOT_direction = Column(String)
    AOT_status = Column(String)
    AWC_signal_index = Column(String)
    AWC_side = Column(String)
    AWC_stop_type = Column(String)
    AWC_price = Column(Float)
    AWC_fees = Column(Float)
    AWC_pnl = Column(Float)
    AWC_return = Column(Float)
    AWC_direction = Column(String)
    AWC_status = Column(String)
    BANPU_signal_index = Column(String)
    BANPU_side = Column(String)
    BANPU_stop_type = Column(String)
    BANPU_price = Column(Float)
    BANPU_fees = Column(Float)
    BANPU_pnl = Column(Float)
    BANPU_return = Column(Float)
    BANPU_direction = Column(String)
    BANPU_status = Column(String)
    BBL_signal_index = Column(String)
    BBL_side = Column(String)
    BBL_stop_type = Column(String)
    BBL_price = Column(Float)
    BBL_fees = Column(Float)
    BBL_pnl = Column(Float)
    BBL_return = Column(Float)
    BBL_direction = Column(String)
    BBL_status = Column(String)
    BDMS_signal_index = Column(String)
    BDMS_side = Column(String)
    BDMS_stop_type = Column(String)
    BDMS_price = Column(Float)
    BDMS_fees = Column(Float)
    BDMS_pnl = Column(Float)
    BDMS_return = Column(Float)
    BDMS_direction = Column(String)
    BDMS_status = Column(String)
    BEM_signal_index = Column(String)
    BEM_side = Column(String)
    BEM_stop_type = Column(String)
    BEM_price = Column(Float)
    BEM_fees = Column(Float)
    BEM_pnl = Column(Float)
    BEM_return = Column(Float)
    BEM_direction = Column(String)
    BEM_status = Column(String)
    BGRIM_signal_index = Column(String)
    BGRIM_side = Column(String)
    BGRIM_stop_type = Column(String)
    BGRIM_price = Column(Float)
    BGRIM_fees = Column(Float)
    BGRIM_pnl = Column(Float)
    BGRIM_return = Column(Float)
    BGRIM_direction = Column(String)
    BGRIM_status = Column(String)
    BH_signal_index = Column(String)
    BH_side = Column(String)
    BH_stop_type = Column(String)
    BH_price = Column(Float)
    BH_fees = Column(Float)
    BH_pnl = Column(Float)
    BH_return = Column(Float)
    BH_direction = Column(String)
    BH_status = Column(String)
    BTS_signal_index = Column(String)
    BTS_side = Column(String)
    BTS_stop_type = Column(String)
    BTS_price = Column(Float)
    BTS_fees = Column(Float)
    BTS_pnl = Column(Float)
    BTS_return = Column(Float)
    BTS_direction = Column(String)
    BTS_status = Column(String)
    CBG_signal_index = Column(String)
    CBG_side = Column(String)
    CBG_stop_type = Column(String)
    CBG_price = Column(Float)
    CBG_fees = Column(Float)
    CBG_pnl = Column(Float)
    CBG_return = Column(Float)
    CBG_direction = Column(String)
    CBG_status = Column(String)
    CENTEL_signal_index = Column(String)
    CENTEL_side = Column(String)
    CENTEL_stop_type = Column(String)
    CENTEL_price = Column(Float)
    CENTEL_fees = Column(Float)
    CENTEL_pnl = Column(Float)
    CENTEL_return = Column(Float)
    CENTEL_direction = Column(String)
    CENTEL_status = Column(String)
    COM7_signal_index = Column(String)
    COM7_side = Column(String)
    COM7_stop_type = Column(String)
    COM7_price = Column(Float)
    COM7_fees = Column(Float)
    COM7_pnl = Column(Float)
    COM7_return = Column(Float)
    COM7_direction = Column(String)
    COM7_status = Column(String)
    CPALL_signal_index = Column(String)
    CPALL_side = Column(String)
    CPALL_stop_type = Column(String)
    CPALL_price = Column(Float)
    CPALL_fees = Column(Float)
    CPALL_pnl = Column(Float)
    CPALL_return = Column(Float)
    CPALL_direction = Column(String)
    CPALL_status = Column(String)
    CPF_signal_index = Column(String)
    CPF_side = Column(String)
    CPF_stop_type = Column(String)
    CPF_price = Column(Float)
    CPF_fees = Column(Float)
    CPF_pnl = Column(Float)
    CPF_return = Column(Float)
    CPF_direction = Column(String)
    CPF_status = Column(String)
    CPN_signal_index = Column(String)
    CPN_side = Column(String)
    CPN_stop_type = Column(String)
    CPN_price = Column(Float)
    CPN_fees = Column(Float)
    CPN_pnl = Column(Float)
    CPN_return = Column(Float)
    CPN_direction = Column(String)
    CPN_status = Column(String)
    CRC_signal_index = Column(String)
    CRC_side = Column(String)
    CRC_stop_type = Column(String)
    CRC_price = Column(Float)
    CRC_fees = Column(Float)
    CRC_pnl = Column(Float)
    CRC_return = Column(Float)
    CRC_direction = Column(String)
    CRC_status = Column(String)
    DELTA_signal_index = Column(String)
    DELTA_side = Column(String)
    DELTA_stop_type = Column(String)
    DELTA_price = Column(Float)
    DELTA_fees = Column(Float)
    DELTA_pnl = Column(Float)
    DELTA_return = Column(Float)
    DELTA_direction = Column(String)
    DELTA_status = Column(String)
    EA_signal_index = Column(String)
    EA_side = Column(String)
    EA_stop_type = Column(String)
    EA_price = Column(Float)
    EA_fees = Column(Float)
    EA_pnl = Column(Float)
    EA_return = Column(Float)
    EA_direction = Column(String)
    EA_status = Column(String)
    EGCO_signal_index = Column(String)
    EGCO_side = Column(String)
    EGCO_stop_type = Column(String)
    EGCO_price = Column(Float)
    EGCO_fees = Column(Float)
    EGCO_pnl = Column(Float)
    EGCO_return = Column(Float)
    EGCO_direction = Column(String)
    EGCO_status = Column(String)
    GLOBAL_signal_index = Column(String)
    GLOBAL_side = Column(String)
    GLOBAL_stop_type = Column(String)
    GLOBAL_price = Column(Float)
    GLOBAL_fees = Column(Float)
    GLOBAL_pnl = Column(Float)
    GLOBAL_return = Column(Float)
    GLOBAL_direction = Column(String)
    GLOBAL_status = Column(String)
    GPSC_signal_index = Column(String)
    GPSC_side = Column(String)
    GPSC_stop_type = Column(String)
    GPSC_price = Column(Float)
    GPSC_fees = Column(Float)
    GPSC_pnl = Column(Float)
    GPSC_return = Column(Float)
    GPSC_direction = Column(String)
    GPSC_status = Column(String)
    GULF_signal_index = Column(String)
    GULF_side = Column(String)
    GULF_stop_type = Column(String)
    GULF_price = Column(Float)
    GULF_fees = Column(Float)
    GULF_pnl = Column(Float)
    GULF_return = Column(Float)
    GULF_direction = Column(String)
    GULF_status = Column(String)
    HMPRO_signal_index = Column(String)
    HMPRO_side = Column(String)
    HMPRO_stop_type = Column(String)
    HMPRO_price = Column(Float)
    HMPRO_fees = Column(Float)
    HMPRO_pnl = Column(Float)
    HMPRO_return = Column(Float)
    HMPRO_direction = Column(String)
    HMPRO_status = Column(String)
    INTUCH_signal_index = Column(String)
    INTUCH_side = Column(String)
    INTUCH_stop_type = Column(String)
    INTUCH_price = Column(Float)
    INTUCH_fees = Column(Float)
    INTUCH_pnl = Column(Float)
    INTUCH_return = Column(Float)
    INTUCH_direction = Column(String)
    INTUCH_status = Column(String)
    IVL_signal_index = Column(String)
    IVL_side = Column(String)
    IVL_stop_type = Column(String)
    IVL_price = Column(Float)
    IVL_fees = Column(Float)
    IVL_pnl = Column(Float)
    IVL_return = Column(Float)
    IVL_direction = Column(String)
    IVL_status = Column(String)
    KBANK_signal_index = Column(String)
    KBANK_side = Column(String)
    KBANK_stop_type = Column(String)
    KBANK_price = Column(Float)
    KBANK_fees = Column(Float)
    KBANK_pnl = Column(Float)
    KBANK_return = Column(Float)
    KBANK_direction = Column(String)
    KBANK_status = Column(String)
    KCE_signal_index = Column(String)
    KCE_side = Column(String)
    KCE_stop_type = Column(String)
    KCE_price = Column(Float)
    KCE_fees = Column(Float)
    KCE_pnl = Column(Float)
    KCE_return = Column(Float)
    KCE_direction = Column(String)
    KCE_status = Column(String)
    KTB_signal_index = Column(String)
    KTB_side = Column(String)
    KTB_stop_type = Column(String)
    KTB_price = Column(Float)
    KTB_fees = Column(Float)
    KTB_pnl = Column(Float)
    KTB_return = Column(Float)
    KTB_direction = Column(String)
    KTB_status = Column(String)
    KTC_signal_index = Column(String)
    KTC_side = Column(String)
    KTC_stop_type = Column(String)
    KTC_price = Column(Float)
    KTC_fees = Column(Float)
    KTC_pnl = Column(Float)
    KTC_return = Column(Float)
    KTC_direction = Column(String)
    KTC_status = Column(String)
    LH_signal_index = Column(String)
    LH_side = Column(String)
    LH_stop_type = Column(String)
    LH_price = Column(Float)
    LH_fees = Column(Float)
    LH_pnl = Column(Float)
    LH_return = Column(Float)
    LH_direction = Column(String)
    LH_status = Column(String)
    MINT_signal_index = Column(String)
    MINT_side = Column(String)
    MINT_stop_type = Column(String)
    MINT_price = Column(Float)
    MINT_fees = Column(Float)
    MINT_pnl = Column(Float)
    MINT_return = Column(Float)
    MINT_direction = Column(String)
    MINT_status = Column(String)
    MTC_signal_index = Column(String)
    MTC_side = Column(String)
    MTC_stop_type = Column(String)
    MTC_price = Column(Float)
    MTC_fees = Column(Float)
    MTC_pnl = Column(Float)
    MTC_return = Column(Float)
    MTC_direction = Column(String)
    MTC_status = Column(String)
    OR_signal_index = Column(String)
    OR_side = Column(String)
    OR_stop_type = Column(String)
    OR_price = Column(Float)
    OR_fees = Column(Float)
    OR_pnl = Column(Float)
    OR_return = Column(Float)
    OR_direction = Column(String)
    OR_status = Column(String)
    OSP_signal_index = Column(String)
    OSP_side = Column(String)
    OSP_stop_type = Column(String)
    OSP_price = Column(Float)
    OSP_fees = Column(Float)
    OSP_pnl = Column(Float)
    OSP_return = Column(Float)
    OSP_direction = Column(String)
    OSP_status = Column(String)
    PTT_signal_index = Column(String)
    PTT_side = Column(String)
    PTT_stop_type = Column(String)
    PTT_price = Column(Float)
    PTT_fees = Column(Float)
    PTT_pnl = Column(Float)
    PTT_return = Column(Float)
    PTT_direction = Column(String)
    PTT_status = Column(String)
    PTTEP_signal_index = Column(String)
    PTTEP_side = Column(String)
    PTTEP_stop_type = Column(String)
    PTTEP_price = Column(Float)
    PTTEP_fees = Column(Float)
    PTTEP_pnl = Column(Float)
    PTTEP_return = Column(Float)
    PTTEP_direction = Column(String)
    PTTEP_status = Column(String)
    PTTGC_signal_index = Column(String)
    PTTGC_side = Column(String)
    PTTGC_stop_type = Column(String)
    PTTGC_price = Column(Float)
    PTTGC_fees = Column(Float)
    PTTGC_pnl = Column(Float)
    PTTGC_return = Column(Float)
    PTTGC_direction = Column(String)
    PTTGC_status = Column(String)
    RATCH_signal_index = Column(String)
    RATCH_side = Column(String)
    RATCH_stop_type = Column(String)
    RATCH_price = Column(Float)
    RATCH_fees = Column(Float)
    RATCH_pnl = Column(Float)
    RATCH_return = Column(Float)
    RATCH_direction = Column(String)
    RATCH_status = Column(String)
    SAWAD_signal_index = Column(String)
    SAWAD_side = Column(String)
    SAWAD_stop_type = Column(String)
    SAWAD_price = Column(Float)
    SAWAD_fees = Column(Float)
    SAWAD_pnl = Column(Float)
    SAWAD_return = Column(Float)
    SAWAD_direction = Column(String)
    SAWAD_status = Column(String)
    SCB_signal_index = Column(String)
    SCB_side = Column(String)
    SCB_stop_type = Column(String)
    SCB_price = Column(Float)
    SCB_fees = Column(Float)
    SCB_pnl = Column(Float)
    SCB_return = Column(Float)
    SCB_direction = Column(String)
    SCB_status = Column(String)
    SCC_signal_index = Column(String)
    SCC_side = Column(String)
    SCC_stop_type = Column(String)
    SCC_price = Column(Float)
    SCC_fees = Column(Float)
    SCC_pnl = Column(Float)
    SCC_return = Column(Float)
    SCC_direction = Column(String)
    SCC_status = Column(String)
    SCGP_signal_index = Column(String)
    SCGP_side = Column(String)
    SCGP_stop_type = Column(String)
    SCGP_price = Column(Float)
    SCGP_fees = Column(Float)
    SCGP_pnl = Column(Float)
    SCGP_return = Column(Float)
    SCGP_direction = Column(String)
    SCGP_status = Column(String)
    TISCO_signal_index = Column(String)
    TISCO_side = Column(String)
    TISCO_stop_type = Column(String)
    TISCO_price = Column(Float)
    TISCO_fees = Column(Float)
    TISCO_pnl = Column(Float)
    TISCO_return = Column(Float)
    TISCO_direction = Column(String)
    TISCO_status = Column(String)
    TOP_signal_index = Column(String)
    TOP_side = Column(String)
    TOP_stop_type = Column(String)
    TOP_price = Column(Float)
    TOP_fees = Column(Float)
    TOP_pnl = Column(Float)
    TOP_return = Column(Float)
    TOP_direction = Column(String)
    TOP_status = Column(String)
    TRUE_signal_index = Column(String)
    TRUE_side = Column(String)
    TRUE_stop_type = Column(String)
    TRUE_price = Column(Float)
    TRUE_fees = Column(Float)
    TRUE_pnl = Column(Float)
    TRUE_return = Column(Float)
    TRUE_direction = Column(String)
    TRUE_status = Column(String)
    TTB_signal_index = Column(String)
    TTB_side = Column(String)
    TTB_stop_type = Column(String)
    TTB_price = Column(Float)
    TTB_fees = Column(Float)
    TTB_pnl = Column(Float)
    TTB_return = Column(Float)
    TTB_direction = Column(String)
    TTB_status = Column(String)
    TU_signal_index = Column(String)
    TU_side = Column(String)
    TU_stop_type = Column(String)
    TU_price = Column(Float)
    TU_fees = Column(Float)
    TU_pnl = Column(Float)
    TU_return = Column(Float)
    TU_direction = Column(String)
    TU_status = Column(String)
    WHA_signal_index = Column(String)
    WHA_side = Column(String)
    WHA_stop_type = Column(String)
    WHA_price = Column(Float)
    WHA_fees = Column(Float)
    WHA_pnl = Column(Float)
    WHA_return = Column(Float)
    WHA_direction = Column(String)
    WHA_status = Column(String)


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
# -------- EMA --------
class EMACROSSClose15T0Sl(BacktestStrategyEMA, Base):
    __tablename__ = "ema_cross_close_15t_0_0"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose15T id={self.id}>"


class EMACROSSClose15T2Sl(BacktestStrategyEMA, Base):
    __tablename__ = "ema_cross_close_15t_2_4"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose15T id={self.id}>"


class EMACROSSClose15T4Sl(BacktestStrategyEMA, Base):
    __tablename__ = "ema_cross_close_15t_4_8"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose15T id={self.id}>"


class EMACROSSClose15T6Sl(BacktestStrategyEMA, Base):
    __tablename__ = "ema_cross_close_15t_6_12"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose15T id={self.id}>"


class EMACROSSClose1H0Sl(BacktestStrategyEMA, Base):
    __tablename__ = "ema_cross_close_1H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose1H id={self.id}>"


class EMACROSSClose1H2Sl(BacktestStrategyEMA, Base):
    __tablename__ = "ema_cross_close_1H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose1H id={self.id}>"


class EMACROSSClose1H4Sl(BacktestStrategyEMA, Base):
    __tablename__ = "ema_cross_close_1H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose1H id={self.id}>"


class EMACROSSClose1H6Sl(BacktestStrategyEMA, Base):
    __tablename__ = "ema_cross_close_1H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose1H id={self.id}>"


class EMACROSSClose4H0Sl(BacktestStrategyEMA, Base):
    __tablename__ = "ema_cross_close_4H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose4H id={self.id}>"


class EMACROSSClose4H2Sl(BacktestStrategyEMA, Base):
    __tablename__ = "ema_cross_close_4H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose4H id={self.id}>"


class EMACROSSClose4H4Sl(BacktestStrategyEMA, Base):
    __tablename__ = "ema_cross_close_4H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose4H id={self.id}>"


class EMACROSSClose4H6Sl(BacktestStrategyEMA, Base):
    __tablename__ = "ema_cross_close_4H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose4H id={self.id}>"


class EMACROSSClose1D0Sl(BacktestStrategyEMA, Base):
    __tablename__ = "ema_cross_close_1D_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose1D id={self.id}>"


class EMACROSSClose1D2Sl(BacktestStrategyEMA, Base):
    __tablename__ = "ema_cross_close_1D_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose1D id={self.id}>"


class EMACROSSClose1D4Sl(BacktestStrategyEMA, Base):
    __tablename__ = "ema_cross_close_1D_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose1D id={self.id}>"


class EMACROSSClose1D6Sl(BacktestStrategyEMA, Base):
    __tablename__ = "ema_cross_close_1D_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACrossClose1D id={self.id}>"

# stats


class EMACROSSStatsClose15T0Sl(StatsStrategy, Base):
    __tablename__ = "ema_cross_stats_close_15t_0_0"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACROSSStatsClose15T id={self.id}>"


class EMACROSSStatsClose15T2Sl(StatsStrategy, Base):
    __tablename__ = "ema_cross_stats_close_15t_2_4"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACROSSStatsClose15T id={self.id}>"


class EMACROSSStatsClose15T4Sl(StatsStrategy, Base):
    __tablename__ = "ema_cross_stats_close_15t_4_8"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACROSSStatsClose15T id={self.id}>"


class EMACROSSStatsClose15T6Sl(StatsStrategy, Base):
    __tablename__ = "ema_cross_stats_close_15t_6_12"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACROSSStatsClose15T id={self.id}>"


class EMACROSSStatsClose1H0Sl(StatsStrategy, Base):
    __tablename__ = "ema_cross_stats_close_1H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACROSSStatsClose1H id={self.id}>"


class EMACROSSStatsClose1H2Sl(StatsStrategy, Base):
    __tablename__ = "ema_cross_stats_close_1H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACROSSStatsClose1H id={self.id}>"


class EMACROSSStatsClose1H4Sl(StatsStrategy, Base):
    __tablename__ = "ema_cross_stats_close_1H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACROSSStatsClose1H id={self.id}>"


class EMACROSSStatsClose1H6Sl(StatsStrategy, Base):
    __tablename__ = "ema_cross_stats_close_1H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACROSSStatsClose1H id={self.id}>"


class EMACROSSStatsClose4H0Sl(StatsStrategy, Base):
    __tablename__ = "ema_cross_stats_close_4H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACROSSStatsClose4H id={self.id}>"


class EMACROSSStatsClose4H2Sl(StatsStrategy, Base):
    __tablename__ = "ema_cross_stats_close_4H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACROSSStatsClose4H id={self.id}>"


class EMACROSSStatsClose4H4Sl(StatsStrategy, Base):
    __tablename__ = "ema_cross_stats_close_4H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACROSSStatsClose4H id={self.id}>"


class EMACROSSStatsClose4H6Sl(StatsStrategy, Base):
    __tablename__ = "ema_cross_stats_close_4H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACROSSStatsClose4H id={self.id}>"


class EMACROSSStatsClose1D0Sl(StatsStrategy, Base):
    __tablename__ = "ema_cross_stats_close_1D_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACROSSStatsClose1D id={self.id}>"


class EMACROSSStatsClose1D2Sl(StatsStrategy, Base):
    __tablename__ = "ema_cross_stats_close_1D_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACROSSStatsClose1D id={self.id}>"


class EMACROSSStatsClose1D4Sl(StatsStrategy, Base):
    __tablename__ = "ema_cross_stats_close_1D_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACROSSStatsClose1D id={self.id}>"


class EMACROSSStatsClose1D6Sl(StatsStrategy, Base):
    __tablename__ = "ema_cross_stats_close_1D_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<EMACROSSStatsClose1D id={self.id}>"

# -------- RSI --------


class RSIClose15T0Sl(BacktestStrategyRSI, Base):
    __tablename__ = "rsi_close_15t_0_0"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIClose15T id={self.id}>"


class RSIClose15T2Sl(BacktestStrategyRSI, Base):
    __tablename__ = "rsi_close_15t_2_4"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIClose15T id={self.id}>"


class RSIClose15T4Sl(BacktestStrategyRSI, Base):
    __tablename__ = "rsi_close_15t_4_8"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIClose15T id={self.id}>"


class RSIClose15T6Sl(BacktestStrategyRSI, Base):
    __tablename__ = "rsi_close_15t_6_12"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIClose15T id={self.id}>"


class RSIClose1H0Sl(BacktestStrategyRSI, Base):
    __tablename__ = "rsi_close_1H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIClose1H id={self.id}>"


class RSIClose1H2Sl(BacktestStrategyRSI, Base):
    __tablename__ = "rsi_close_1H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIClose1H id={self.id}>"


class RSIClose1H4Sl(BacktestStrategyRSI, Base):
    __tablename__ = "rsi_close_1H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIClose1H id={self.id}>"


class RSIClose1H6Sl(BacktestStrategyRSI, Base):
    __tablename__ = "rsi_close_1H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIClose1H id={self.id}>"


class RSIClose4H0Sl(BacktestStrategyRSI, Base):
    __tablename__ = "rsi_close_4H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIClose4H id={self.id}>"


class RSIClose4H2Sl(BacktestStrategyRSI, Base):
    __tablename__ = "rsi_close_4H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIClose4H id={self.id}>"


class RSIClose4H4Sl(BacktestStrategyRSI, Base):
    __tablename__ = "rsi_close_4H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIClose4H id={self.id}>"


class RSIClose4H6Sl(BacktestStrategyRSI, Base):
    __tablename__ = "rsi_close_4H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIClose4H id={self.id}>"


class RSIClose1D0Sl(BacktestStrategyRSI, Base):
    __tablename__ = "rsi_close_1D_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIClose1D id={self.id}>"


class RSIClose1D2Sl(BacktestStrategyRSI, Base):
    __tablename__ = "rsi_close_1D_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIClose1D id={self.id}>"


class RSIClose1D4Sl(BacktestStrategyRSI, Base):
    __tablename__ = "rsi_close_1D_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIClose1D id={self.id}>"


class RSIClose1D6Sl(BacktestStrategyRSI, Base):
    __tablename__ = "rsi_close_1D_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIClose1D id={self.id}>"

# stats


class RSIStatsClose15T0Sl(StatsStrategy, Base):
    __tablename__ = "rsi_stats_close_15t_0_0"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIStatsClose15T id={self.id}>"


class RSIStatsClose15T2Sl(StatsStrategy, Base):
    __tablename__ = "rsi_stats_close_15t_2_4"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIStatsClose15T id={self.id}>"


class RSIStatsClose15T4Sl(StatsStrategy, Base):
    __tablename__ = "rsi_stats_close_15t_4_8"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIStatsClose15T id={self.id}>"


class RSIStatsClose15T6Sl(StatsStrategy, Base):
    __tablename__ = "rsi_stats_close_15t_6_12"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIStatsClose15T id={self.id}>"


class RSIStatsClose1H0Sl(StatsStrategy, Base):
    __tablename__ = "rsi_stats_close_1H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIStatsClose1H id={self.id}>"


class RSIStatsClose1H2Sl(StatsStrategy, Base):
    __tablename__ = "rsi_stats_close_1H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIStatsClose1H id={self.id}>"


class RSIStatsClose1H4Sl(StatsStrategy, Base):
    __tablename__ = "rsi_stats_close_1H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIStatsClose1H id={self.id}>"


class RSIStatsClose1H6Sl(StatsStrategy, Base):
    __tablename__ = "rsi_stats_close_1H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIStatsClose1H id={self.id}>"


class RSIStatsClose4H0Sl(StatsStrategy, Base):
    __tablename__ = "rsi_stats_close_4H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIStatsClose4H id={self.id}>"


class RSIStatsClose4H2Sl(StatsStrategy, Base):
    __tablename__ = "rsi_stats_close_4H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIStatsClose4H id={self.id}>"


class RSIStatsClose4H4Sl(StatsStrategy, Base):
    __tablename__ = "rsi_stats_close_4H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIStatsClose4H id={self.id}>"


class RSIStatsClose4H6Sl(StatsStrategy, Base):
    __tablename__ = "rsi_stats_close_4H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIStatsClose4H id={self.id}>"


class RSIStatsClose1D0Sl(StatsStrategy, Base):
    __tablename__ = "rsi_stats_close_1D_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIStatsClose1D id={self.id}>"


class RSIStatsClose1D2Sl(StatsStrategy, Base):
    __tablename__ = "rsi_stats_close_1D_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIStatsClose1D id={self.id}>"


class RSIStatsClose1D4Sl(StatsStrategy, Base):
    __tablename__ = "rsi_stats_close_1D_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIStatsClose1D id={self.id}>"


class RSIStatsClose1D6Sl(StatsStrategy, Base):
    __tablename__ = "rsi_stats_close_1D_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<RSIStatsClose1D id={self.id}>"


class MACDClose15T0Sl(BacktestStrategyMACD, Base):
    __tablename__ = "macd_close_15T_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDClose15T id={self.id}>"


class MACDClose15T2Sl(BacktestStrategyMACD, Base):
    __tablename__ = "macd_close_15T_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDClose15T id={self.id}>"


class MACDClose15T4Sl(BacktestStrategyMACD, Base):
    __tablename__ = "macd_close_15T_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDClose15T id={self.id}>"


class MACDClose15T6Sl(BacktestStrategyMACD, Base):
    __tablename__ = "macd_close_15T_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDClose15T id={self.id}>"


class MACDClose1H0Sl(BacktestStrategyMACD, Base):
    __tablename__ = "macd_close_1H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDClose1H id={self.id}>"


class MACDClose1H2Sl(BacktestStrategyMACD, Base):
    __tablename__ = "macd_close_1H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDClose1H id={self.id}>"


class MACDClose1H4Sl(BacktestStrategyMACD, Base):
    __tablename__ = "macd_close_1H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDClose1H id={self.id}>"


class MACDClose1H6Sl(BacktestStrategyMACD, Base):
    __tablename__ = "macd_close_1H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDClose1H id={self.id}>"


class MACDClose4H0Sl(BacktestStrategyMACD, Base):
    __tablename__ = "macd_close_4H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDClose4H id={self.id}>"


class MACDClose4H2Sl(BacktestStrategyMACD, Base):
    __tablename__ = "macd_close_4H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDClose4H id={self.id}>"


class MACDClose4H4Sl(BacktestStrategyMACD, Base):
    __tablename__ = "macd_close_4H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDClose4H id={self.id}>"


class MACDClose4H6Sl(BacktestStrategyMACD, Base):
    __tablename__ = "macd_close_4H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDClose4H id={self.id}>"


class MACDClose1D0Sl(BacktestStrategyMACD, Base):
    __tablename__ = "macd_close_1D_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDClose1D id={self.id}>"


class MACDClose1D2Sl(BacktestStrategyMACD, Base):
    __tablename__ = "macd_close_1D_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDClose1D id={self.id}>"


class MACDClose1D4Sl(BacktestStrategyMACD, Base):
    __tablename__ = "macd_close_1D_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDClose1D id={self.id}>"


class MACDClose1D6Sl(BacktestStrategyMACD, Base):
    __tablename__ = "macd_close_1D_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDClose1D id={self.id}>"


class MACDStatsClose15T0Sl(StatsStrategy, Base):
    __tablename__ = "macd_stats_close_15T_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDStatsClose15T id={self.id}>"


class MACDStatsClose15T2Sl(StatsStrategy, Base):
    __tablename__ = "macd_stats_close_15T_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDStatsClose15T id={self.id}>"


class MACDStatsClose15T4Sl(StatsStrategy, Base):
    __tablename__ = "macd_stats_close_15T_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDStatsClose15T id={self.id}>"


class MACDStatsClose15T6Sl(StatsStrategy, Base):
    __tablename__ = "macd_stats_close_15T_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDStatsClose15T id={self.id}>"


class MACDStatsClose1H0Sl(StatsStrategy, Base):
    __tablename__ = "macd_stats_close_1H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDStatsClose1H id={self.id}>"


class MACDStatsClose1H2Sl(StatsStrategy, Base):
    __tablename__ = "macd_stats_close_1H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDStatsClose1H id={self.id}>"


class MACDStatsClose1H4Sl(StatsStrategy, Base):
    __tablename__ = "macd_stats_close_1H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDStatsClose1H id={self.id}>"


class MACDStatsClose1H6Sl(StatsStrategy, Base):
    __tablename__ = "macd_stats_close_1H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDStatsClose1H id={self.id}>"


class MACDStatsClose4H0Sl(StatsStrategy, Base):
    __tablename__ = "macd_stats_close_4H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDStatsClose4H id={self.id}>"


class MACDStatsClose4H2Sl(StatsStrategy, Base):
    __tablename__ = "macd_stats_close_4H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDStatsClose4H id={self.id}>"


class MACDStatsClose4H4Sl(StatsStrategy, Base):
    __tablename__ = "macd_stats_close_4H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDStatsClose4H id={self.id}>"


class MACDStatsClose4H6Sl(StatsStrategy, Base):
    __tablename__ = "macd_stats_close_4H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDStatsClose4H id={self.id}>"


class MACDStatsClose1D0Sl(StatsStrategy, Base):
    __tablename__ = "macd_stats_close_1D_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDStatsClose1D id={self.id}>"


class MACDStatsClose1D2Sl(StatsStrategy, Base):
    __tablename__ = "macd_stats_close_1D_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDStatsClose1D id={self.id}>"


class MACDStatsClose1D4Sl(StatsStrategy, Base):
    __tablename__ = "macd_stats_close_1D_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDStatsClose1D id={self.id}>"


class MACDStatsClose1D6Sl(StatsStrategy, Base):
    __tablename__ = "macd_stats_close_1D_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<MACDStatsClose1D id={self.id}>"
# ------------- Compare Table ------------


class CompareTable(Base):
    __tablename__ = "trading_stats_compare"
    id = Column(Integer, primary_key=True)

    index = Column(String)
    ADVANC_fund = Column(String)
    AOT_fund = Column(String)
    AWC_fund = Column(String)
    BANPU_fund = Column(String)
    BBL_fund = Column(String)
    BDMS_fund = Column(String)
    BEM_fund = Column(String)
    BGRIM_fund = Column(String)
    BH_fund = Column(String)
    BTS_fund = Column(String)
    CBG_fund = Column(String)
    CENTEL_fund = Column(String)
    COM7_fund = Column(String)
    CPALL_fund = Column(String)
    CPF_fund = Column(String)
    CPN_fund = Column(String)
    CRC_fund = Column(String)
    DELTA_fund = Column(String)
    EA_fund = Column(String)
    EGCO_fund = Column(String)
    GLOBAL_fund = Column(String)
    GPSC_fund = Column(String)
    GULF_fund = Column(String)
    HMPRO_fund = Column(String)
    INTUCH_fund = Column(String)
    IVL_fund = Column(String)
    KBANK_fund = Column(String)
    KCE_fund = Column(String)
    KTB_fund = Column(String)
    KTC_fund = Column(String)
    LH_fund = Column(String)
    MINT_fund = Column(String)
    MTC_fund = Column(String)
    OR_fund = Column(String)
    OSP_fund = Column(String)
    PTT_fund = Column(String)
    PTTEP_fund = Column(String)
    PTTGC_fund = Column(String)
    RATCH_fund = Column(String)
    SAWAD_fund = Column(String)
    SCB_fund = Column(String)
    SCC_fund = Column(String)
    SCGP_fund = Column(String)
    TISCO_fund = Column(String)
    TOP_fund = Column(String)
    TRUE_fund = Column(String)
    TTB_fund = Column(String)
    TU_fund = Column(String)
    WHA_fund = Column(String)

    def __repr__(self):
        return f"<CompareTable id={self.id}>"


class SpecificInfo(Base):
    __tablename__ = "specific_info"

    id = Column(Integer, primary_key=True)
    index = Column(String)
    ADVANC = Column(String)
    AOT = Column(String)
    AWC = Column(String)
    BANPU = Column(String)
    BBL = Column(String)
    BDMS = Column(String)
    BEM = Column(String)
    BGRIM = Column(String)
    BH = Column(String)
    BTS = Column(String)
    CBG = Column(String)
    CENTEL = Column(String)
    COM7 = Column(String)
    CPALL = Column(String)
    CPF = Column(String)
    CPN = Column(String)
    CRC = Column(String)
    DELTA = Column(String)
    EA = Column(String)
    EGCO = Column(String)
    GLOBAL = Column(String)
    GPSC = Column(String)
    GULF = Column(String)
    HMPRO = Column(String)
    INTUCH = Column(String)
    IVL = Column(String)
    KBANK = Column(String)
    KCE = Column(String)
    KTB = Column(String)
    KTC = Column(String)
    LH = Column(String)
    MINT = Column(String)
    MTC = Column(String)
    OR = Column(String)
    OSP = Column(String)
    PTT = Column(String)
    PTTEP = Column(String)
    PTTGC = Column(String)
    RATCH = Column(String)
    SAWAD = Column(String)
    SCB = Column(String)
    SCC = Column(String)
    SCGP = Column(String)
    TISCO = Column(String)
    TOP = Column(String)
    TRUE = Column(String)
    TTB = Column(String)
    TU = Column(String)
    WHA = Column(String)

# --------- Trade History EMA---------
# 15T


class TradeHistoryEMACROSS15T0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_ema_cross_close_15t_0_0"
    id = Column(Integer, primary_key=True)


class TradeHistoryEMACROSS15T2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_ema_cross_close_15t_2_4"
    id = Column(Integer, primary_key=True)


class TradeHistoryEMACROSS15T4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_ema_cross_close_15t_4_8"
    id = Column(Integer, primary_key=True)


class TradeHistoryEMACROSS15T6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_ema_cross_close_15t_6_12"
    id = Column(Integer, primary_key=True)
# 1H


class TradeHistoryEMACROSS1H0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_ema_cross_close_1h_0_0"
    id = Column(Integer, primary_key=True)


class TradeHistoryEMACROSS1H2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_ema_cross_close_1h_2_4"
    id = Column(Integer, primary_key=True)


class TradeHistoryEMACROSS1H4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_ema_cross_close_1h_4_8"
    id = Column(Integer, primary_key=True)


class TradeHistoryEMACROSS1H6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_ema_cross_close_1h_6_12"
    id = Column(Integer, primary_key=True)

# 4H


class TradeHistoryEMACROSS4H0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_ema_cross_close_4h_0_0"
    id = Column(Integer, primary_key=True)


class TradeHistoryEMACROSS4H2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_ema_cross_close_4h_2_4"
    id = Column(Integer, primary_key=True)


class TradeHistoryEMACROSS4H4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_ema_cross_close_4h_4_8"
    id = Column(Integer, primary_key=True)


class TradeHistoryEMACROSS4H6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_ema_cross_close_4h_6_12"
    id = Column(Integer, primary_key=True)

# 1D


class TradeHistoryEMACROSS1D0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_ema_cross_close_1d_0_0"
    id = Column(Integer, primary_key=True)


class TradeHistoryEMACROSS1D2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_ema_cross_close_1d_2_4"
    id = Column(Integer, primary_key=True)


class TradeHistoryEMACROSS1D4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_ema_cross_close_1d_4_8"
    id = Column(Integer, primary_key=True)


class TradeHistoryEMACROSS1D6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_ema_cross_close_1d_6_12"
    id = Column(Integer, primary_key=True)

# --------- Trade History RSI---------
# 15T


class TradeHistoryRSI15T0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_RSI_close_15t_0_0".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryRSI15T2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_RSI_close_15t_2_4".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryRSI15T4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_RSI_close_15t_4_8".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryRSI15T6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_RSI_close_15t_6_12".lower()
    id = Column(Integer, primary_key=True)
# 1H


class TradeHistoryRSI1H0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_RSI_close_1h_0_0".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryRSI1H2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_RSI_close_1h_2_4".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryRSI1H4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_RSI_close_1h_4_8".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryRSI1H6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_RSI_close_1h_6_12".lower()
    id = Column(Integer, primary_key=True)

# 4H


class TradeHistoryRSI4H0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_RSI_close_4h_0_0".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryRSI4H2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_RSI_close_4h_2_4".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryRSI4H4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_RSI_close_4h_4_8".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryRSI4H6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_RSI_close_4h_6_12".lower()
    id = Column(Integer, primary_key=True)

# 1D


class TradeHistoryRSI1D0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_RSI_close_1d_0_0".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryRSI1D2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_RSI_close_1d_2_4".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryRSI1D4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_RSI_close_1d_4_8".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryRSI1D6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_RSI_close_1d_6_12".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryMACD15T0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_macd_close_15T_0_0"
    id = Column(Integer, primary_key=True)


class TradeHistoryMACD15T2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_macd_close_15T_2_4"
    id = Column(Integer, primary_key=True)


class TradeHistoryMACD15T4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_macd_close_15T_4_8"
    id = Column(Integer, primary_key=True)


class TradeHistoryMACD15T6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_macd_close_15T_6_12"
    id = Column(Integer, primary_key=True)


class TradeHistoryMACD1H0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_macd_close_1H_0_0"
    id = Column(Integer, primary_key=True)


class TradeHistoryMACD1H2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_macd_close_1H_2_4"
    id = Column(Integer, primary_key=True)


class TradeHistoryMACD1H4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_macd_close_1H_4_8"
    id = Column(Integer, primary_key=True)


class TradeHistoryMACD1H6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_macd_close_1H_6_12"
    id = Column(Integer, primary_key=True)


class TradeHistoryMACD4H0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_macd_close_4H_0_0"
    id = Column(Integer, primary_key=True)


class TradeHistoryMACD4H2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_macd_close_4H_2_4"
    id = Column(Integer, primary_key=True)


class TradeHistoryMACD4H4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_macd_close_4H_4_8"
    id = Column(Integer, primary_key=True)


class TradeHistoryMACD4H6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_macd_close_4H_6_12"
    id = Column(Integer, primary_key=True)


class TradeHistoryMACD1D0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_macd_close_1D_0_0"
    id = Column(Integer, primary_key=True)


class TradeHistoryMACD1D2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_macd_close_1D_2_4"
    id = Column(Integer, primary_key=True)


class TradeHistoryMACD1D4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_macd_close_1D_4_8"
    id = Column(Integer, primary_key=True)


class TradeHistoryMACD1D6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_macd_close_1D_6_12"
    id = Column(Integer, primary_key=True)


# -------------- ADX HERE -------------------


class BacktestStrategyADX():
    ADVANC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    ADVANC_open = Column(Float)
    ADVANC_high = Column(Float)
    ADVANC_low = Column(Float)
    ADVANC_close = Column(Float)
    ADVANC_volume = Column(Integer)
    ADVANC_adx = Column(Float)
    ADVANC_buy_signal = Column(Boolean, unique=False, default=True)
    ADVANC_sell_signal = Column(Boolean, unique=False, default=True)
    ADVANC_green_signal = Column(Float)
    ADVANC_red_signal = Column(Float)
    AOT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    AOT_open = Column(Float)
    AOT_high = Column(Float)
    AOT_low = Column(Float)
    AOT_close = Column(Float)
    AOT_volume = Column(Integer)
    AOT_adx = Column(Float)
    AOT_buy_signal = Column(Boolean, unique=False, default=True)
    AOT_sell_signal = Column(Boolean, unique=False, default=True)
    AOT_green_signal = Column(Float)
    AOT_red_signal = Column(Float)
    AWC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    AWC_open = Column(Float)
    AWC_high = Column(Float)
    AWC_low = Column(Float)
    AWC_close = Column(Float)
    AWC_volume = Column(Integer)
    AWC_adx = Column(Float)
    AWC_buy_signal = Column(Boolean, unique=False, default=True)
    AWC_sell_signal = Column(Boolean, unique=False, default=True)
    AWC_green_signal = Column(Float)
    AWC_red_signal = Column(Float)
    BANPU_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BANPU_open = Column(Float)
    BANPU_high = Column(Float)
    BANPU_low = Column(Float)
    BANPU_close = Column(Float)
    BANPU_volume = Column(Integer)
    BANPU_adx = Column(Float)
    BANPU_buy_signal = Column(Boolean, unique=False, default=True)
    BANPU_sell_signal = Column(Boolean, unique=False, default=True)
    BANPU_green_signal = Column(Float)
    BANPU_red_signal = Column(Float)
    BBL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BBL_open = Column(Float)
    BBL_high = Column(Float)
    BBL_low = Column(Float)
    BBL_close = Column(Float)
    BBL_volume = Column(Integer)
    BBL_adx = Column(Float)
    BBL_buy_signal = Column(Boolean, unique=False, default=True)
    BBL_sell_signal = Column(Boolean, unique=False, default=True)
    BBL_green_signal = Column(Float)
    BBL_red_signal = Column(Float)
    BDMS_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BDMS_open = Column(Float)
    BDMS_high = Column(Float)
    BDMS_low = Column(Float)
    BDMS_close = Column(Float)
    BDMS_volume = Column(Integer)
    BDMS_adx = Column(Float)
    BDMS_buy_signal = Column(Boolean, unique=False, default=True)
    BDMS_sell_signal = Column(Boolean, unique=False, default=True)
    BDMS_green_signal = Column(Float)
    BDMS_red_signal = Column(Float)
    BEM_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BEM_open = Column(Float)
    BEM_high = Column(Float)
    BEM_low = Column(Float)
    BEM_close = Column(Float)
    BEM_volume = Column(Integer)
    BEM_adx = Column(Float)
    BEM_buy_signal = Column(Boolean, unique=False, default=True)
    BEM_sell_signal = Column(Boolean, unique=False, default=True)
    BEM_green_signal = Column(Float)
    BEM_red_signal = Column(Float)
    BGRIM_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BGRIM_open = Column(Float)
    BGRIM_high = Column(Float)
    BGRIM_low = Column(Float)
    BGRIM_close = Column(Float)
    BGRIM_volume = Column(Integer)
    BGRIM_adx = Column(Float)
    BGRIM_buy_signal = Column(Boolean, unique=False, default=True)
    BGRIM_sell_signal = Column(Boolean, unique=False, default=True)
    BGRIM_green_signal = Column(Float)
    BGRIM_red_signal = Column(Float)
    BH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BH_open = Column(Float)
    BH_high = Column(Float)
    BH_low = Column(Float)
    BH_close = Column(Float)
    BH_volume = Column(Integer)
    BH_adx = Column(Float)
    BH_buy_signal = Column(Boolean, unique=False, default=True)
    BH_sell_signal = Column(Boolean, unique=False, default=True)
    BH_green_signal = Column(Float)
    BH_red_signal = Column(Float)
    BTS_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BTS_open = Column(Float)
    BTS_high = Column(Float)
    BTS_low = Column(Float)
    BTS_close = Column(Float)
    BTS_volume = Column(Integer)
    BTS_adx = Column(Float)
    BTS_buy_signal = Column(Boolean, unique=False, default=True)
    BTS_sell_signal = Column(Boolean, unique=False, default=True)
    BTS_green_signal = Column(Float)
    BTS_red_signal = Column(Float)
    CBG_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CBG_open = Column(Float)
    CBG_high = Column(Float)
    CBG_low = Column(Float)
    CBG_close = Column(Float)
    CBG_volume = Column(Integer)
    CBG_adx = Column(Float)
    CBG_buy_signal = Column(Boolean, unique=False, default=True)
    CBG_sell_signal = Column(Boolean, unique=False, default=True)
    CBG_green_signal = Column(Float)
    CBG_red_signal = Column(Float)
    CENTEL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CENTEL_open = Column(Float)
    CENTEL_high = Column(Float)
    CENTEL_low = Column(Float)
    CENTEL_close = Column(Float)
    CENTEL_volume = Column(Integer)
    CENTEL_adx = Column(Float)
    CENTEL_buy_signal = Column(Boolean, unique=False, default=True)
    CENTEL_sell_signal = Column(Boolean, unique=False, default=True)
    CENTEL_green_signal = Column(Float)
    CENTEL_red_signal = Column(Float)
    COM7_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    COM7_open = Column(Float)
    COM7_high = Column(Float)
    COM7_low = Column(Float)
    COM7_close = Column(Float)
    COM7_volume = Column(Integer)
    COM7_adx = Column(Float)
    COM7_buy_signal = Column(Boolean, unique=False, default=True)
    COM7_sell_signal = Column(Boolean, unique=False, default=True)
    COM7_green_signal = Column(Float)
    COM7_red_signal = Column(Float)
    CPALL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPALL_open = Column(Float)
    CPALL_high = Column(Float)
    CPALL_low = Column(Float)
    CPALL_close = Column(Float)
    CPALL_volume = Column(Integer)
    CPALL_adx = Column(Float)
    CPALL_buy_signal = Column(Boolean, unique=False, default=True)
    CPALL_sell_signal = Column(Boolean, unique=False, default=True)
    CPALL_green_signal = Column(Float)
    CPALL_red_signal = Column(Float)
    CPF_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPF_open = Column(Float)
    CPF_high = Column(Float)
    CPF_low = Column(Float)
    CPF_close = Column(Float)
    CPF_volume = Column(Integer)
    CPF_adx = Column(Float)
    CPF_buy_signal = Column(Boolean, unique=False, default=True)
    CPF_sell_signal = Column(Boolean, unique=False, default=True)
    CPF_green_signal = Column(Float)
    CPF_red_signal = Column(Float)
    CPN_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPN_open = Column(Float)
    CPN_high = Column(Float)
    CPN_low = Column(Float)
    CPN_close = Column(Float)
    CPN_volume = Column(Integer)
    CPN_adx = Column(Float)
    CPN_buy_signal = Column(Boolean, unique=False, default=True)
    CPN_sell_signal = Column(Boolean, unique=False, default=True)
    CPN_green_signal = Column(Float)
    CPN_red_signal = Column(Float)
    CRC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CRC_open = Column(Float)
    CRC_high = Column(Float)
    CRC_low = Column(Float)
    CRC_close = Column(Float)
    CRC_volume = Column(Integer)
    CRC_adx = Column(Float)
    CRC_buy_signal = Column(Boolean, unique=False, default=True)
    CRC_sell_signal = Column(Boolean, unique=False, default=True)
    CRC_green_signal = Column(Float)
    CRC_red_signal = Column(Float)
    DELTA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    DELTA_open = Column(Float)
    DELTA_high = Column(Float)
    DELTA_low = Column(Float)
    DELTA_close = Column(Float)
    DELTA_volume = Column(Integer)
    DELTA_adx = Column(Float)
    DELTA_buy_signal = Column(Boolean, unique=False, default=True)
    DELTA_sell_signal = Column(Boolean, unique=False, default=True)
    DELTA_green_signal = Column(Float)
    DELTA_red_signal = Column(Float)
    EA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    EA_open = Column(Float)
    EA_high = Column(Float)
    EA_low = Column(Float)
    EA_close = Column(Float)
    EA_volume = Column(Integer)
    EA_adx = Column(Float)
    EA_buy_signal = Column(Boolean, unique=False, default=True)
    EA_sell_signal = Column(Boolean, unique=False, default=True)
    EA_green_signal = Column(Float)
    EA_red_signal = Column(Float)
    EGCO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    EGCO_open = Column(Float)
    EGCO_high = Column(Float)
    EGCO_low = Column(Float)
    EGCO_close = Column(Float)
    EGCO_volume = Column(Integer)
    EGCO_adx = Column(Float)
    EGCO_buy_signal = Column(Boolean, unique=False, default=True)
    EGCO_sell_signal = Column(Boolean, unique=False, default=True)
    EGCO_green_signal = Column(Float)
    EGCO_red_signal = Column(Float)
    GLOBAL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GLOBAL_open = Column(Float)
    GLOBAL_high = Column(Float)
    GLOBAL_low = Column(Float)
    GLOBAL_close = Column(Float)
    GLOBAL_volume = Column(Integer)
    GLOBAL_adx = Column(Float)
    GLOBAL_buy_signal = Column(Boolean, unique=False, default=True)
    GLOBAL_sell_signal = Column(Boolean, unique=False, default=True)
    GLOBAL_green_signal = Column(Float)
    GLOBAL_red_signal = Column(Float)
    GPSC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GPSC_open = Column(Float)
    GPSC_high = Column(Float)
    GPSC_low = Column(Float)
    GPSC_close = Column(Float)
    GPSC_volume = Column(Integer)
    GPSC_adx = Column(Float)
    GPSC_buy_signal = Column(Boolean, unique=False, default=True)
    GPSC_sell_signal = Column(Boolean, unique=False, default=True)
    GPSC_green_signal = Column(Float)
    GPSC_red_signal = Column(Float)
    GULF_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GULF_open = Column(Float)
    GULF_high = Column(Float)
    GULF_low = Column(Float)
    GULF_close = Column(Float)
    GULF_volume = Column(Integer)
    GULF_adx = Column(Float)
    GULF_buy_signal = Column(Boolean, unique=False, default=True)
    GULF_sell_signal = Column(Boolean, unique=False, default=True)
    GULF_green_signal = Column(Float)
    GULF_red_signal = Column(Float)
    HMPRO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    HMPRO_open = Column(Float)
    HMPRO_high = Column(Float)
    HMPRO_low = Column(Float)
    HMPRO_close = Column(Float)
    HMPRO_volume = Column(Integer)
    HMPRO_adx = Column(Float)
    HMPRO_buy_signal = Column(Boolean, unique=False, default=True)
    HMPRO_sell_signal = Column(Boolean, unique=False, default=True)
    HMPRO_green_signal = Column(Float)
    HMPRO_red_signal = Column(Float)
    INTUCH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    INTUCH_open = Column(Float)
    INTUCH_high = Column(Float)
    INTUCH_low = Column(Float)
    INTUCH_close = Column(Float)
    INTUCH_volume = Column(Integer)
    INTUCH_adx = Column(Float)
    INTUCH_buy_signal = Column(Boolean, unique=False, default=True)
    INTUCH_sell_signal = Column(Boolean, unique=False, default=True)
    INTUCH_green_signal = Column(Float)
    INTUCH_red_signal = Column(Float)
    IVL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    IVL_open = Column(Float)
    IVL_high = Column(Float)
    IVL_low = Column(Float)
    IVL_close = Column(Float)
    IVL_volume = Column(Integer)
    IVL_adx = Column(Float)
    IVL_buy_signal = Column(Boolean, unique=False, default=True)
    IVL_sell_signal = Column(Boolean, unique=False, default=True)
    IVL_green_signal = Column(Float)
    IVL_red_signal = Column(Float)
    KBANK_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KBANK_open = Column(Float)
    KBANK_high = Column(Float)
    KBANK_low = Column(Float)
    KBANK_close = Column(Float)
    KBANK_volume = Column(Integer)
    KBANK_adx = Column(Float)
    KBANK_buy_signal = Column(Boolean, unique=False, default=True)
    KBANK_sell_signal = Column(Boolean, unique=False, default=True)
    KBANK_green_signal = Column(Float)
    KBANK_red_signal = Column(Float)
    KCE_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KCE_open = Column(Float)
    KCE_high = Column(Float)
    KCE_low = Column(Float)
    KCE_close = Column(Float)
    KCE_volume = Column(Integer)
    KCE_adx = Column(Float)
    KCE_buy_signal = Column(Boolean, unique=False, default=True)
    KCE_sell_signal = Column(Boolean, unique=False, default=True)
    KCE_green_signal = Column(Float)
    KCE_red_signal = Column(Float)
    KTB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KTB_open = Column(Float)
    KTB_high = Column(Float)
    KTB_low = Column(Float)
    KTB_close = Column(Float)
    KTB_volume = Column(Integer)
    KTB_adx = Column(Float)
    KTB_buy_signal = Column(Boolean, unique=False, default=True)
    KTB_sell_signal = Column(Boolean, unique=False, default=True)
    KTB_green_signal = Column(Float)
    KTB_red_signal = Column(Float)
    KTC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KTC_open = Column(Float)
    KTC_high = Column(Float)
    KTC_low = Column(Float)
    KTC_close = Column(Float)
    KTC_volume = Column(Integer)
    KTC_adx = Column(Float)
    KTC_buy_signal = Column(Boolean, unique=False, default=True)
    KTC_sell_signal = Column(Boolean, unique=False, default=True)
    KTC_green_signal = Column(Float)
    KTC_red_signal = Column(Float)
    LH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    LH_open = Column(Float)
    LH_high = Column(Float)
    LH_low = Column(Float)
    LH_close = Column(Float)
    LH_volume = Column(Integer)
    LH_adx = Column(Float)
    LH_buy_signal = Column(Boolean, unique=False, default=True)
    LH_sell_signal = Column(Boolean, unique=False, default=True)
    LH_green_signal = Column(Float)
    LH_red_signal = Column(Float)
    MINT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    MINT_open = Column(Float)
    MINT_high = Column(Float)
    MINT_low = Column(Float)
    MINT_close = Column(Float)
    MINT_volume = Column(Integer)
    MINT_adx = Column(Float)
    MINT_buy_signal = Column(Boolean, unique=False, default=True)
    MINT_sell_signal = Column(Boolean, unique=False, default=True)
    MINT_green_signal = Column(Float)
    MINT_red_signal = Column(Float)
    MTC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    MTC_open = Column(Float)
    MTC_high = Column(Float)
    MTC_low = Column(Float)
    MTC_close = Column(Float)
    MTC_volume = Column(Integer)
    MTC_adx = Column(Float)
    MTC_buy_signal = Column(Boolean, unique=False, default=True)
    MTC_sell_signal = Column(Boolean, unique=False, default=True)
    MTC_green_signal = Column(Float)
    MTC_red_signal = Column(Float)
    OR_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    OR_open = Column(Float)
    OR_high = Column(Float)
    OR_low = Column(Float)
    OR_close = Column(Float)
    OR_volume = Column(Integer)
    OR_adx = Column(Float)
    OR_buy_signal = Column(Boolean, unique=False, default=True)
    OR_sell_signal = Column(Boolean, unique=False, default=True)
    OR_green_signal = Column(Float)
    OR_red_signal = Column(Float)
    OSP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    OSP_open = Column(Float)
    OSP_high = Column(Float)
    OSP_low = Column(Float)
    OSP_close = Column(Float)
    OSP_volume = Column(Integer)
    OSP_adx = Column(Float)
    OSP_buy_signal = Column(Boolean, unique=False, default=True)
    OSP_sell_signal = Column(Boolean, unique=False, default=True)
    OSP_green_signal = Column(Float)
    OSP_red_signal = Column(Float)
    PTT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTT_open = Column(Float)
    PTT_high = Column(Float)
    PTT_low = Column(Float)
    PTT_close = Column(Float)
    PTT_volume = Column(Integer)
    PTT_adx = Column(Float)
    PTT_buy_signal = Column(Boolean, unique=False, default=True)
    PTT_sell_signal = Column(Boolean, unique=False, default=True)
    PTT_green_signal = Column(Float)
    PTT_red_signal = Column(Float)
    PTTEP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTTEP_open = Column(Float)
    PTTEP_high = Column(Float)
    PTTEP_low = Column(Float)
    PTTEP_close = Column(Float)
    PTTEP_volume = Column(Integer)
    PTTEP_adx = Column(Float)
    PTTEP_buy_signal = Column(Boolean, unique=False, default=True)
    PTTEP_sell_signal = Column(Boolean, unique=False, default=True)
    PTTEP_green_signal = Column(Float)
    PTTEP_red_signal = Column(Float)
    PTTGC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTTGC_open = Column(Float)
    PTTGC_high = Column(Float)
    PTTGC_low = Column(Float)
    PTTGC_close = Column(Float)
    PTTGC_volume = Column(Integer)
    PTTGC_adx = Column(Float)
    PTTGC_buy_signal = Column(Boolean, unique=False, default=True)
    PTTGC_sell_signal = Column(Boolean, unique=False, default=True)
    PTTGC_green_signal = Column(Float)
    PTTGC_red_signal = Column(Float)
    RATCH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    RATCH_open = Column(Float)
    RATCH_high = Column(Float)
    RATCH_low = Column(Float)
    RATCH_close = Column(Float)
    RATCH_volume = Column(Integer)
    RATCH_adx = Column(Float)
    RATCH_buy_signal = Column(Boolean, unique=False, default=True)
    RATCH_sell_signal = Column(Boolean, unique=False, default=True)
    RATCH_green_signal = Column(Float)
    RATCH_red_signal = Column(Float)
    SAWAD_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SAWAD_open = Column(Float)
    SAWAD_high = Column(Float)
    SAWAD_low = Column(Float)
    SAWAD_close = Column(Float)
    SAWAD_volume = Column(Integer)
    SAWAD_adx = Column(Float)
    SAWAD_buy_signal = Column(Boolean, unique=False, default=True)
    SAWAD_sell_signal = Column(Boolean, unique=False, default=True)
    SAWAD_green_signal = Column(Float)
    SAWAD_red_signal = Column(Float)
    SCB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCB_open = Column(Float)
    SCB_high = Column(Float)
    SCB_low = Column(Float)
    SCB_close = Column(Float)
    SCB_volume = Column(Integer)
    SCB_adx = Column(Float)
    SCB_buy_signal = Column(Boolean, unique=False, default=True)
    SCB_sell_signal = Column(Boolean, unique=False, default=True)
    SCB_green_signal = Column(Float)
    SCB_red_signal = Column(Float)
    SCC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCC_open = Column(Float)
    SCC_high = Column(Float)
    SCC_low = Column(Float)
    SCC_close = Column(Float)
    SCC_volume = Column(Integer)
    SCC_adx = Column(Float)
    SCC_buy_signal = Column(Boolean, unique=False, default=True)
    SCC_sell_signal = Column(Boolean, unique=False, default=True)
    SCC_green_signal = Column(Float)
    SCC_red_signal = Column(Float)
    SCGP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCGP_open = Column(Float)
    SCGP_high = Column(Float)
    SCGP_low = Column(Float)
    SCGP_close = Column(Float)
    SCGP_volume = Column(Integer)
    SCGP_adx = Column(Float)
    SCGP_buy_signal = Column(Boolean, unique=False, default=True)
    SCGP_sell_signal = Column(Boolean, unique=False, default=True)
    SCGP_green_signal = Column(Float)
    SCGP_red_signal = Column(Float)
    TISCO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TISCO_open = Column(Float)
    TISCO_high = Column(Float)
    TISCO_low = Column(Float)
    TISCO_close = Column(Float)
    TISCO_volume = Column(Integer)
    TISCO_adx = Column(Float)
    TISCO_buy_signal = Column(Boolean, unique=False, default=True)
    TISCO_sell_signal = Column(Boolean, unique=False, default=True)
    TISCO_green_signal = Column(Float)
    TISCO_red_signal = Column(Float)
    TOP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TOP_open = Column(Float)
    TOP_high = Column(Float)
    TOP_low = Column(Float)
    TOP_close = Column(Float)
    TOP_volume = Column(Integer)
    TOP_adx = Column(Float)
    TOP_buy_signal = Column(Boolean, unique=False, default=True)
    TOP_sell_signal = Column(Boolean, unique=False, default=True)
    TOP_green_signal = Column(Float)
    TOP_red_signal = Column(Float)
    TRUE_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TRUE_open = Column(Float)
    TRUE_high = Column(Float)
    TRUE_low = Column(Float)
    TRUE_close = Column(Float)
    TRUE_volume = Column(Integer)
    TRUE_adx = Column(Float)
    TRUE_buy_signal = Column(Boolean, unique=False, default=True)
    TRUE_sell_signal = Column(Boolean, unique=False, default=True)
    TRUE_green_signal = Column(Float)
    TRUE_red_signal = Column(Float)
    TTB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TTB_open = Column(Float)
    TTB_high = Column(Float)
    TTB_low = Column(Float)
    TTB_close = Column(Float)
    TTB_volume = Column(Integer)
    TTB_adx = Column(Float)
    TTB_buy_signal = Column(Boolean, unique=False, default=True)
    TTB_sell_signal = Column(Boolean, unique=False, default=True)
    TTB_green_signal = Column(Float)
    TTB_red_signal = Column(Float)
    TU_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TU_open = Column(Float)
    TU_high = Column(Float)
    TU_low = Column(Float)
    TU_close = Column(Float)
    TU_volume = Column(Integer)
    TU_adx = Column(Float)
    TU_buy_signal = Column(Boolean, unique=False, default=True)
    TU_sell_signal = Column(Boolean, unique=False, default=True)
    TU_green_signal = Column(Float)
    TU_red_signal = Column(Float)
    WHA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    WHA_open = Column(Float)
    WHA_high = Column(Float)
    WHA_low = Column(Float)
    WHA_close = Column(Float)
    WHA_volume = Column(Integer)
    WHA_adx = Column(Float)
    WHA_buy_signal = Column(Boolean, unique=False, default=True)
    WHA_sell_signal = Column(Boolean, unique=False, default=True)
    WHA_green_signal = Column(Float)
    WHA_red_signal = Column(Float)


class ADXClose15T0Sl(BacktestStrategyADX, Base):
    __tablename__ = "adx_close_15T_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXClose15T id={self.id}>"


class ADXClose15T2Sl(BacktestStrategyADX, Base):
    __tablename__ = "adx_close_15T_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXClose15T id={self.id}>"


class ADXClose15T4Sl(BacktestStrategyADX, Base):
    __tablename__ = "adx_close_15T_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXClose15T id={self.id}>"


class ADXClose15T6Sl(BacktestStrategyADX, Base):
    __tablename__ = "adx_close_15T_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXClose15T id={self.id}>"


class ADXClose1H0Sl(BacktestStrategyADX, Base):
    __tablename__ = "adx_close_1H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXClose1H id={self.id}>"


class ADXClose1H2Sl(BacktestStrategyADX, Base):
    __tablename__ = "adx_close_1H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXClose1H id={self.id}>"


class ADXClose1H4Sl(BacktestStrategyADX, Base):
    __tablename__ = "adx_close_1H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXClose1H id={self.id}>"


class ADXClose1H6Sl(BacktestStrategyADX, Base):
    __tablename__ = "adx_close_1H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXClose1H id={self.id}>"


class ADXClose4H0Sl(BacktestStrategyADX, Base):
    __tablename__ = "adx_close_4H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXClose4H id={self.id}>"


class ADXClose4H2Sl(BacktestStrategyADX, Base):
    __tablename__ = "adx_close_4H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXClose4H id={self.id}>"


class ADXClose4H4Sl(BacktestStrategyADX, Base):
    __tablename__ = "adx_close_4H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXClose4H id={self.id}>"


class ADXClose4H6Sl(BacktestStrategyADX, Base):
    __tablename__ = "adx_close_4H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXClose4H id={self.id}>"


class ADXClose1D0Sl(BacktestStrategyADX, Base):
    __tablename__ = "adx_close_1D_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXClose1D id={self.id}>"


class ADXClose1D2Sl(BacktestStrategyADX, Base):
    __tablename__ = "adx_close_1D_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXClose1D id={self.id}>"


class ADXClose1D4Sl(BacktestStrategyADX, Base):
    __tablename__ = "adx_close_1D_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXClose1D id={self.id}>"


class ADXClose1D6Sl(BacktestStrategyADX, Base):
    __tablename__ = "adx_close_1D_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXClose1D id={self.id}>"


class ADXStatsClose15T0Sl(StatsStrategy, Base):
    __tablename__ = "ADX_stats_close_15T_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXStatsClose15T id={self.id}>"


class ADXStatsClose15T2Sl(StatsStrategy, Base):
    __tablename__ = "ADX_stats_close_15T_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXStatsClose15T id={self.id}>"


class ADXStatsClose15T4Sl(StatsStrategy, Base):
    __tablename__ = "ADX_stats_close_15T_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXStatsClose15T id={self.id}>"


class ADXStatsClose15T6Sl(StatsStrategy, Base):
    __tablename__ = "ADX_stats_close_15T_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXStatsClose15T id={self.id}>"


class ADXStatsClose1H0Sl(StatsStrategy, Base):
    __tablename__ = "ADX_stats_close_1H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXStatsClose1H id={self.id}>"


class ADXStatsClose1H2Sl(StatsStrategy, Base):
    __tablename__ = "ADX_stats_close_1H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXStatsClose1H id={self.id}>"


class ADXStatsClose1H4Sl(StatsStrategy, Base):
    __tablename__ = "ADX_stats_close_1H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXStatsClose1H id={self.id}>"


class ADXStatsClose1H6Sl(StatsStrategy, Base):
    __tablename__ = "ADX_stats_close_1H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXStatsClose1H id={self.id}>"


class ADXStatsClose4H0Sl(StatsStrategy, Base):
    __tablename__ = "ADX_stats_close_4H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXStatsClose4H id={self.id}>"


class ADXStatsClose4H2Sl(StatsStrategy, Base):
    __tablename__ = "ADX_stats_close_4H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXStatsClose4H id={self.id}>"


class ADXStatsClose4H4Sl(StatsStrategy, Base):
    __tablename__ = "ADX_stats_close_4H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXStatsClose4H id={self.id}>"


class ADXStatsClose4H6Sl(StatsStrategy, Base):
    __tablename__ = "ADX_stats_close_4H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXStatsClose4H id={self.id}>"


class ADXStatsClose1D0Sl(StatsStrategy, Base):
    __tablename__ = "ADX_stats_close_1D_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXStatsClose1D id={self.id}>"


class ADXStatsClose1D2Sl(StatsStrategy, Base):
    __tablename__ = "ADX_stats_close_1D_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXStatsClose1D id={self.id}>"


class ADXStatsClose1D4Sl(StatsStrategy, Base):
    __tablename__ = "ADX_stats_close_1D_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXStatsClose1D id={self.id}>"


class ADXStatsClose1D6Sl(StatsStrategy, Base):
    __tablename__ = "ADX_stats_close_1D_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ADXStatsClose1D id={self.id}>"


class TradeHistoryADX15T0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_adx_close_15T_0_0"
    id = Column(Integer, primary_key=True)


class TradeHistoryADX15T2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_adx_close_15T_2_4"
    id = Column(Integer, primary_key=True)


class TradeHistoryADX15T4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_adx_close_15T_4_8"
    id = Column(Integer, primary_key=True)


class TradeHistoryADX15T6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_adx_close_15T_6_12"
    id = Column(Integer, primary_key=True)


class TradeHistoryADX1H0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_adx_close_1H_0_0"
    id = Column(Integer, primary_key=True)


class TradeHistoryADX1H2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_adx_close_1H_2_4"
    id = Column(Integer, primary_key=True)


class TradeHistoryADX1H4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_adx_close_1H_4_8"
    id = Column(Integer, primary_key=True)


class TradeHistoryADX1H6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_adx_close_1H_6_12"
    id = Column(Integer, primary_key=True)


class TradeHistoryADX4H0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_adx_close_4H_0_0"
    id = Column(Integer, primary_key=True)


class TradeHistoryADX4H2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_adx_close_4H_2_4"
    id = Column(Integer, primary_key=True)


class TradeHistoryADX4H4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_adx_close_4H_4_8"
    id = Column(Integer, primary_key=True)


class TradeHistoryADX4H6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_adx_close_4H_6_12"
    id = Column(Integer, primary_key=True)


class TradeHistoryADX1D0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_adx_close_1D_0_0"
    id = Column(Integer, primary_key=True)


class TradeHistoryADX1D2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_adx_close_1D_2_4"
    id = Column(Integer, primary_key=True)


class TradeHistoryADX1D4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_adx_close_1D_4_8"
    id = Column(Integer, primary_key=True)


class TradeHistoryADX1D6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_adx_close_1D_6_12"
    id = Column(Integer, primary_key=True)


# ---------- BBANDS -------------------
class BacktestStrategyBBANDS():
    ADVANC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    ADVANC_open = Column(Float)
    ADVANC_high = Column(Float)
    ADVANC_low = Column(Float)
    ADVANC_close = Column(Float)
    ADVANC_volume = Column(Integer)
    ADVANC_buy_signal = Column(Boolean, unique=False, default=True)
    ADVANC_sell_signal = Column(Boolean, unique=False, default=True)
    ADVANC_green_signal = Column(Float)
    ADVANC_red_signal = Column(Float)
    AOT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    AOT_open = Column(Float)
    AOT_high = Column(Float)
    AOT_low = Column(Float)
    AOT_close = Column(Float)
    AOT_volume = Column(Integer)
    AOT_buy_signal = Column(Boolean, unique=False, default=True)
    AOT_sell_signal = Column(Boolean, unique=False, default=True)
    AOT_green_signal = Column(Float)
    AOT_red_signal = Column(Float)
    AWC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    AWC_open = Column(Float)
    AWC_high = Column(Float)
    AWC_low = Column(Float)
    AWC_close = Column(Float)
    AWC_volume = Column(Integer)
    AWC_buy_signal = Column(Boolean, unique=False, default=True)
    AWC_sell_signal = Column(Boolean, unique=False, default=True)
    AWC_green_signal = Column(Float)
    AWC_red_signal = Column(Float)
    BANPU_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BANPU_open = Column(Float)
    BANPU_high = Column(Float)
    BANPU_low = Column(Float)
    BANPU_close = Column(Float)
    BANPU_volume = Column(Integer)
    BANPU_buy_signal = Column(Boolean, unique=False, default=True)
    BANPU_sell_signal = Column(Boolean, unique=False, default=True)
    BANPU_green_signal = Column(Float)
    BANPU_red_signal = Column(Float)
    BBL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BBL_open = Column(Float)
    BBL_high = Column(Float)
    BBL_low = Column(Float)
    BBL_close = Column(Float)
    BBL_volume = Column(Integer)
    BBL_buy_signal = Column(Boolean, unique=False, default=True)
    BBL_sell_signal = Column(Boolean, unique=False, default=True)
    BBL_green_signal = Column(Float)
    BBL_red_signal = Column(Float)
    BDMS_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BDMS_open = Column(Float)
    BDMS_high = Column(Float)
    BDMS_low = Column(Float)
    BDMS_close = Column(Float)
    BDMS_volume = Column(Integer)
    BDMS_buy_signal = Column(Boolean, unique=False, default=True)
    BDMS_sell_signal = Column(Boolean, unique=False, default=True)
    BDMS_green_signal = Column(Float)
    BDMS_red_signal = Column(Float)
    BEM_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BEM_open = Column(Float)
    BEM_high = Column(Float)
    BEM_low = Column(Float)
    BEM_close = Column(Float)
    BEM_volume = Column(Integer)
    BEM_buy_signal = Column(Boolean, unique=False, default=True)
    BEM_sell_signal = Column(Boolean, unique=False, default=True)
    BEM_green_signal = Column(Float)
    BEM_red_signal = Column(Float)
    BGRIM_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BGRIM_open = Column(Float)
    BGRIM_high = Column(Float)
    BGRIM_low = Column(Float)
    BGRIM_close = Column(Float)
    BGRIM_volume = Column(Integer)
    BGRIM_buy_signal = Column(Boolean, unique=False, default=True)
    BGRIM_sell_signal = Column(Boolean, unique=False, default=True)
    BGRIM_green_signal = Column(Float)
    BGRIM_red_signal = Column(Float)
    BH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BH_open = Column(Float)
    BH_high = Column(Float)
    BH_low = Column(Float)
    BH_close = Column(Float)
    BH_volume = Column(Integer)
    BH_buy_signal = Column(Boolean, unique=False, default=True)
    BH_sell_signal = Column(Boolean, unique=False, default=True)
    BH_green_signal = Column(Float)
    BH_red_signal = Column(Float)
    BTS_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    BTS_open = Column(Float)
    BTS_high = Column(Float)
    BTS_low = Column(Float)
    BTS_close = Column(Float)
    BTS_volume = Column(Integer)
    BTS_buy_signal = Column(Boolean, unique=False, default=True)
    BTS_sell_signal = Column(Boolean, unique=False, default=True)
    BTS_green_signal = Column(Float)
    BTS_red_signal = Column(Float)
    CBG_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CBG_open = Column(Float)
    CBG_high = Column(Float)
    CBG_low = Column(Float)
    CBG_close = Column(Float)
    CBG_volume = Column(Integer)
    CBG_buy_signal = Column(Boolean, unique=False, default=True)
    CBG_sell_signal = Column(Boolean, unique=False, default=True)
    CBG_green_signal = Column(Float)
    CBG_red_signal = Column(Float)
    CENTEL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CENTEL_open = Column(Float)
    CENTEL_high = Column(Float)
    CENTEL_low = Column(Float)
    CENTEL_close = Column(Float)
    CENTEL_volume = Column(Integer)
    CENTEL_buy_signal = Column(Boolean, unique=False, default=True)
    CENTEL_sell_signal = Column(Boolean, unique=False, default=True)
    CENTEL_green_signal = Column(Float)
    CENTEL_red_signal = Column(Float)
    COM7_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    COM7_open = Column(Float)
    COM7_high = Column(Float)
    COM7_low = Column(Float)
    COM7_close = Column(Float)
    COM7_volume = Column(Integer)
    COM7_buy_signal = Column(Boolean, unique=False, default=True)
    COM7_sell_signal = Column(Boolean, unique=False, default=True)
    COM7_green_signal = Column(Float)
    COM7_red_signal = Column(Float)
    CPALL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPALL_open = Column(Float)
    CPALL_high = Column(Float)
    CPALL_low = Column(Float)
    CPALL_close = Column(Float)
    CPALL_volume = Column(Integer)
    CPALL_buy_signal = Column(Boolean, unique=False, default=True)
    CPALL_sell_signal = Column(Boolean, unique=False, default=True)
    CPALL_green_signal = Column(Float)
    CPALL_red_signal = Column(Float)
    CPF_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPF_open = Column(Float)
    CPF_high = Column(Float)
    CPF_low = Column(Float)
    CPF_close = Column(Float)
    CPF_volume = Column(Integer)
    CPF_buy_signal = Column(Boolean, unique=False, default=True)
    CPF_sell_signal = Column(Boolean, unique=False, default=True)
    CPF_green_signal = Column(Float)
    CPF_red_signal = Column(Float)
    CPN_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CPN_open = Column(Float)
    CPN_high = Column(Float)
    CPN_low = Column(Float)
    CPN_close = Column(Float)
    CPN_volume = Column(Integer)
    CPN_buy_signal = Column(Boolean, unique=False, default=True)
    CPN_sell_signal = Column(Boolean, unique=False, default=True)
    CPN_green_signal = Column(Float)
    CPN_red_signal = Column(Float)
    CRC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    CRC_open = Column(Float)
    CRC_high = Column(Float)
    CRC_low = Column(Float)
    CRC_close = Column(Float)
    CRC_volume = Column(Integer)
    CRC_buy_signal = Column(Boolean, unique=False, default=True)
    CRC_sell_signal = Column(Boolean, unique=False, default=True)
    CRC_green_signal = Column(Float)
    CRC_red_signal = Column(Float)
    DELTA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    DELTA_open = Column(Float)
    DELTA_high = Column(Float)
    DELTA_low = Column(Float)
    DELTA_close = Column(Float)
    DELTA_volume = Column(Integer)
    DELTA_buy_signal = Column(Boolean, unique=False, default=True)
    DELTA_sell_signal = Column(Boolean, unique=False, default=True)
    DELTA_green_signal = Column(Float)
    DELTA_red_signal = Column(Float)
    EA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    EA_open = Column(Float)
    EA_high = Column(Float)
    EA_low = Column(Float)
    EA_close = Column(Float)
    EA_volume = Column(Integer)
    EA_buy_signal = Column(Boolean, unique=False, default=True)
    EA_sell_signal = Column(Boolean, unique=False, default=True)
    EA_green_signal = Column(Float)
    EA_red_signal = Column(Float)
    EGCO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    EGCO_open = Column(Float)
    EGCO_high = Column(Float)
    EGCO_low = Column(Float)
    EGCO_close = Column(Float)
    EGCO_volume = Column(Integer)
    EGCO_buy_signal = Column(Boolean, unique=False, default=True)
    EGCO_sell_signal = Column(Boolean, unique=False, default=True)
    EGCO_green_signal = Column(Float)
    EGCO_red_signal = Column(Float)
    GLOBAL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GLOBAL_open = Column(Float)
    GLOBAL_high = Column(Float)
    GLOBAL_low = Column(Float)
    GLOBAL_close = Column(Float)
    GLOBAL_volume = Column(Integer)
    GLOBAL_buy_signal = Column(Boolean, unique=False, default=True)
    GLOBAL_sell_signal = Column(Boolean, unique=False, default=True)
    GLOBAL_green_signal = Column(Float)
    GLOBAL_red_signal = Column(Float)
    GPSC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GPSC_open = Column(Float)
    GPSC_high = Column(Float)
    GPSC_low = Column(Float)
    GPSC_close = Column(Float)
    GPSC_volume = Column(Integer)
    GPSC_buy_signal = Column(Boolean, unique=False, default=True)
    GPSC_sell_signal = Column(Boolean, unique=False, default=True)
    GPSC_green_signal = Column(Float)
    GPSC_red_signal = Column(Float)
    GULF_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    GULF_open = Column(Float)
    GULF_high = Column(Float)
    GULF_low = Column(Float)
    GULF_close = Column(Float)
    GULF_volume = Column(Integer)
    GULF_buy_signal = Column(Boolean, unique=False, default=True)
    GULF_sell_signal = Column(Boolean, unique=False, default=True)
    GULF_green_signal = Column(Float)
    GULF_red_signal = Column(Float)
    HMPRO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    HMPRO_open = Column(Float)
    HMPRO_high = Column(Float)
    HMPRO_low = Column(Float)
    HMPRO_close = Column(Float)
    HMPRO_volume = Column(Integer)
    HMPRO_buy_signal = Column(Boolean, unique=False, default=True)
    HMPRO_sell_signal = Column(Boolean, unique=False, default=True)
    HMPRO_green_signal = Column(Float)
    HMPRO_red_signal = Column(Float)
    INTUCH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    INTUCH_open = Column(Float)
    INTUCH_high = Column(Float)
    INTUCH_low = Column(Float)
    INTUCH_close = Column(Float)
    INTUCH_volume = Column(Integer)
    INTUCH_buy_signal = Column(Boolean, unique=False, default=True)
    INTUCH_sell_signal = Column(Boolean, unique=False, default=True)
    INTUCH_green_signal = Column(Float)
    INTUCH_red_signal = Column(Float)
    IVL_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    IVL_open = Column(Float)
    IVL_high = Column(Float)
    IVL_low = Column(Float)
    IVL_close = Column(Float)
    IVL_volume = Column(Integer)
    IVL_buy_signal = Column(Boolean, unique=False, default=True)
    IVL_sell_signal = Column(Boolean, unique=False, default=True)
    IVL_green_signal = Column(Float)
    IVL_red_signal = Column(Float)
    KBANK_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KBANK_open = Column(Float)
    KBANK_high = Column(Float)
    KBANK_low = Column(Float)
    KBANK_close = Column(Float)
    KBANK_volume = Column(Integer)
    KBANK_buy_signal = Column(Boolean, unique=False, default=True)
    KBANK_sell_signal = Column(Boolean, unique=False, default=True)
    KBANK_green_signal = Column(Float)
    KBANK_red_signal = Column(Float)
    KCE_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KCE_open = Column(Float)
    KCE_high = Column(Float)
    KCE_low = Column(Float)
    KCE_close = Column(Float)
    KCE_volume = Column(Integer)
    KCE_buy_signal = Column(Boolean, unique=False, default=True)
    KCE_sell_signal = Column(Boolean, unique=False, default=True)
    KCE_green_signal = Column(Float)
    KCE_red_signal = Column(Float)
    KTB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KTB_open = Column(Float)
    KTB_high = Column(Float)
    KTB_low = Column(Float)
    KTB_close = Column(Float)
    KTB_volume = Column(Integer)
    KTB_buy_signal = Column(Boolean, unique=False, default=True)
    KTB_sell_signal = Column(Boolean, unique=False, default=True)
    KTB_green_signal = Column(Float)
    KTB_red_signal = Column(Float)
    KTC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    KTC_open = Column(Float)
    KTC_high = Column(Float)
    KTC_low = Column(Float)
    KTC_close = Column(Float)
    KTC_volume = Column(Integer)
    KTC_buy_signal = Column(Boolean, unique=False, default=True)
    KTC_sell_signal = Column(Boolean, unique=False, default=True)
    KTC_green_signal = Column(Float)
    KTC_red_signal = Column(Float)
    LH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    LH_open = Column(Float)
    LH_high = Column(Float)
    LH_low = Column(Float)
    LH_close = Column(Float)
    LH_volume = Column(Integer)
    LH_buy_signal = Column(Boolean, unique=False, default=True)
    LH_sell_signal = Column(Boolean, unique=False, default=True)
    LH_green_signal = Column(Float)
    LH_red_signal = Column(Float)
    MINT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    MINT_open = Column(Float)
    MINT_high = Column(Float)
    MINT_low = Column(Float)
    MINT_close = Column(Float)
    MINT_volume = Column(Integer)
    MINT_buy_signal = Column(Boolean, unique=False, default=True)
    MINT_sell_signal = Column(Boolean, unique=False, default=True)
    MINT_green_signal = Column(Float)
    MINT_red_signal = Column(Float)
    MTC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    MTC_open = Column(Float)
    MTC_high = Column(Float)
    MTC_low = Column(Float)
    MTC_close = Column(Float)
    MTC_volume = Column(Integer)
    MTC_buy_signal = Column(Boolean, unique=False, default=True)
    MTC_sell_signal = Column(Boolean, unique=False, default=True)
    MTC_green_signal = Column(Float)
    MTC_red_signal = Column(Float)
    OR_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    OR_open = Column(Float)
    OR_high = Column(Float)
    OR_low = Column(Float)
    OR_close = Column(Float)
    OR_volume = Column(Integer)
    OR_buy_signal = Column(Boolean, unique=False, default=True)
    OR_sell_signal = Column(Boolean, unique=False, default=True)
    OR_green_signal = Column(Float)
    OR_red_signal = Column(Float)
    OSP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    OSP_open = Column(Float)
    OSP_high = Column(Float)
    OSP_low = Column(Float)
    OSP_close = Column(Float)
    OSP_volume = Column(Integer)
    OSP_buy_signal = Column(Boolean, unique=False, default=True)
    OSP_sell_signal = Column(Boolean, unique=False, default=True)
    OSP_green_signal = Column(Float)
    OSP_red_signal = Column(Float)
    PTT_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTT_open = Column(Float)
    PTT_high = Column(Float)
    PTT_low = Column(Float)
    PTT_close = Column(Float)
    PTT_volume = Column(Integer)
    PTT_buy_signal = Column(Boolean, unique=False, default=True)
    PTT_sell_signal = Column(Boolean, unique=False, default=True)
    PTT_green_signal = Column(Float)
    PTT_red_signal = Column(Float)
    PTTEP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTTEP_open = Column(Float)
    PTTEP_high = Column(Float)
    PTTEP_low = Column(Float)
    PTTEP_close = Column(Float)
    PTTEP_volume = Column(Integer)
    PTTEP_buy_signal = Column(Boolean, unique=False, default=True)
    PTTEP_sell_signal = Column(Boolean, unique=False, default=True)
    PTTEP_green_signal = Column(Float)
    PTTEP_red_signal = Column(Float)
    PTTGC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    PTTGC_open = Column(Float)
    PTTGC_high = Column(Float)
    PTTGC_low = Column(Float)
    PTTGC_close = Column(Float)
    PTTGC_volume = Column(Integer)
    PTTGC_buy_signal = Column(Boolean, unique=False, default=True)
    PTTGC_sell_signal = Column(Boolean, unique=False, default=True)
    PTTGC_green_signal = Column(Float)
    PTTGC_red_signal = Column(Float)
    RATCH_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    RATCH_open = Column(Float)
    RATCH_high = Column(Float)
    RATCH_low = Column(Float)
    RATCH_close = Column(Float)
    RATCH_volume = Column(Integer)
    RATCH_buy_signal = Column(Boolean, unique=False, default=True)
    RATCH_sell_signal = Column(Boolean, unique=False, default=True)
    RATCH_green_signal = Column(Float)
    RATCH_red_signal = Column(Float)
    SAWAD_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SAWAD_open = Column(Float)
    SAWAD_high = Column(Float)
    SAWAD_low = Column(Float)
    SAWAD_close = Column(Float)
    SAWAD_volume = Column(Integer)
    SAWAD_buy_signal = Column(Boolean, unique=False, default=True)
    SAWAD_sell_signal = Column(Boolean, unique=False, default=True)
    SAWAD_green_signal = Column(Float)
    SAWAD_red_signal = Column(Float)
    SCB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCB_open = Column(Float)
    SCB_high = Column(Float)
    SCB_low = Column(Float)
    SCB_close = Column(Float)
    SCB_volume = Column(Integer)
    SCB_buy_signal = Column(Boolean, unique=False, default=True)
    SCB_sell_signal = Column(Boolean, unique=False, default=True)
    SCB_green_signal = Column(Float)
    SCB_red_signal = Column(Float)
    SCC_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCC_open = Column(Float)
    SCC_high = Column(Float)
    SCC_low = Column(Float)
    SCC_close = Column(Float)
    SCC_volume = Column(Integer)
    SCC_buy_signal = Column(Boolean, unique=False, default=True)
    SCC_sell_signal = Column(Boolean, unique=False, default=True)
    SCC_green_signal = Column(Float)
    SCC_red_signal = Column(Float)
    SCGP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    SCGP_open = Column(Float)
    SCGP_high = Column(Float)
    SCGP_low = Column(Float)
    SCGP_close = Column(Float)
    SCGP_volume = Column(Integer)
    SCGP_buy_signal = Column(Boolean, unique=False, default=True)
    SCGP_sell_signal = Column(Boolean, unique=False, default=True)
    SCGP_green_signal = Column(Float)
    SCGP_red_signal = Column(Float)
    TISCO_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TISCO_open = Column(Float)
    TISCO_high = Column(Float)
    TISCO_low = Column(Float)
    TISCO_close = Column(Float)
    TISCO_volume = Column(Integer)
    TISCO_buy_signal = Column(Boolean, unique=False, default=True)
    TISCO_sell_signal = Column(Boolean, unique=False, default=True)
    TISCO_green_signal = Column(Float)
    TISCO_red_signal = Column(Float)
    TOP_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TOP_open = Column(Float)
    TOP_high = Column(Float)
    TOP_low = Column(Float)
    TOP_close = Column(Float)
    TOP_volume = Column(Integer)
    TOP_buy_signal = Column(Boolean, unique=False, default=True)
    TOP_sell_signal = Column(Boolean, unique=False, default=True)
    TOP_green_signal = Column(Float)
    TOP_red_signal = Column(Float)
    TRUE_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TRUE_open = Column(Float)
    TRUE_high = Column(Float)
    TRUE_low = Column(Float)
    TRUE_close = Column(Float)
    TRUE_volume = Column(Integer)
    TRUE_buy_signal = Column(Boolean, unique=False, default=True)
    TRUE_sell_signal = Column(Boolean, unique=False, default=True)
    TRUE_green_signal = Column(Float)
    TRUE_red_signal = Column(Float)
    TTB_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TTB_open = Column(Float)
    TTB_high = Column(Float)
    TTB_low = Column(Float)
    TTB_close = Column(Float)
    TTB_volume = Column(Integer)
    TTB_buy_signal = Column(Boolean, unique=False, default=True)
    TTB_sell_signal = Column(Boolean, unique=False, default=True)
    TTB_green_signal = Column(Float)
    TTB_red_signal = Column(Float)
    TU_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    TU_open = Column(Float)
    TU_high = Column(Float)
    TU_low = Column(Float)
    TU_close = Column(Float)
    TU_volume = Column(Integer)
    TU_buy_signal = Column(Boolean, unique=False, default=True)
    TU_sell_signal = Column(Boolean, unique=False, default=True)
    TU_green_signal = Column(Float)
    TU_red_signal = Column(Float)
    WHA_datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d" +
        "%(hour)02d:%(minute)02d:%(second)02d"),
        default=datetime.datetime.utcnow)
    WHA_open = Column(Float)
    WHA_high = Column(Float)
    WHA_low = Column(Float)
    WHA_close = Column(Float)
    WHA_volume = Column(Integer)
    WHA_buy_signal = Column(Boolean, unique=False, default=True)
    WHA_sell_signal = Column(Boolean, unique=False, default=True)
    WHA_green_signal = Column(Float)
    WHA_red_signal = Column(Float)


class BBANDSClose15T0Sl(BacktestStrategyBBANDS, Base):
    __tablename__ = "bbands_close_15T_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSClose15T id={self.id}>"


class BBANDSClose15T2Sl(BacktestStrategyBBANDS, Base):
    __tablename__ = "bbands_close_15T_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSClose15T id={self.id}>"


class BBANDSClose15T4Sl(BacktestStrategyBBANDS, Base):
    __tablename__ = "bbands_close_15T_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSClose15T id={self.id}>"


class BBANDSClose15T6Sl(BacktestStrategyBBANDS, Base):
    __tablename__ = "bbands_close_15T_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSClose15T id={self.id}>"


class BBANDSClose1H0Sl(BacktestStrategyBBANDS, Base):
    __tablename__ = "bbands_close_1H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSClose1H id={self.id}>"


class BBANDSClose1H2Sl(BacktestStrategyBBANDS, Base):
    __tablename__ = "bbands_close_1H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSClose1H id={self.id}>"


class BBANDSClose1H4Sl(BacktestStrategyBBANDS, Base):
    __tablename__ = "bbands_close_1H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSClose1H id={self.id}>"


class BBANDSClose1H6Sl(BacktestStrategyBBANDS, Base):
    __tablename__ = "bbands_close_1H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSClose1H id={self.id}>"


class BBANDSClose4H0Sl(BacktestStrategyBBANDS, Base):
    __tablename__ = "bbands_close_4H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSClose4H id={self.id}>"


class BBANDSClose4H2Sl(BacktestStrategyBBANDS, Base):
    __tablename__ = "bbands_close_4H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSClose4H id={self.id}>"


class BBANDSClose4H4Sl(BacktestStrategyBBANDS, Base):
    __tablename__ = "bbands_close_4H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSClose4H id={self.id}>"


class BBANDSClose4H6Sl(BacktestStrategyBBANDS, Base):
    __tablename__ = "bbands_close_4H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSClose4H id={self.id}>"


class BBANDSClose1D0Sl(BacktestStrategyBBANDS, Base):
    __tablename__ = "bbands_close_1D_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSClose1D id={self.id}>"


class BBANDSClose1D2Sl(BacktestStrategyBBANDS, Base):
    __tablename__ = "bbands_close_1D_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSClose1D id={self.id}>"


class BBANDSClose1D4Sl(BacktestStrategyBBANDS, Base):
    __tablename__ = "bbands_close_1D_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSClose1D id={self.id}>"


class BBANDSClose1D6Sl(BacktestStrategyBBANDS, Base):
    __tablename__ = "bbands_close_1D_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSClose1D id={self.id}>"


class BBANDSStatsClose15T0Sl(StatsStrategy, Base):
    __tablename__ = "BBANDS_stats_close_15T_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSStatsClose15T id={self.id}>"


class BBANDSStatsClose15T2Sl(StatsStrategy, Base):
    __tablename__ = "BBANDS_stats_close_15T_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSStatsClose15T id={self.id}>"


class BBANDSStatsClose15T4Sl(StatsStrategy, Base):
    __tablename__ = "BBANDS_stats_close_15T_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSStatsClose15T id={self.id}>"


class BBANDSStatsClose15T6Sl(StatsStrategy, Base):
    __tablename__ = "BBANDS_stats_close_15T_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSStatsClose15T id={self.id}>"


class BBANDSStatsClose1H0Sl(StatsStrategy, Base):
    __tablename__ = "BBANDS_stats_close_1H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSStatsClose1H id={self.id}>"


class BBANDSStatsClose1H2Sl(StatsStrategy, Base):
    __tablename__ = "BBANDS_stats_close_1H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSStatsClose1H id={self.id}>"


class BBANDSStatsClose1H4Sl(StatsStrategy, Base):
    __tablename__ = "BBANDS_stats_close_1H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSStatsClose1H id={self.id}>"


class BBANDSStatsClose1H6Sl(StatsStrategy, Base):
    __tablename__ = "BBANDS_stats_close_1H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSStatsClose1H id={self.id}>"


class BBANDSStatsClose4H0Sl(StatsStrategy, Base):
    __tablename__ = "BBANDS_stats_close_4H_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSStatsClose4H id={self.id}>"


class BBANDSStatsClose4H2Sl(StatsStrategy, Base):
    __tablename__ = "BBANDS_stats_close_4H_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSStatsClose4H id={self.id}>"


class BBANDSStatsClose4H4Sl(StatsStrategy, Base):
    __tablename__ = "BBANDS_stats_close_4H_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSStatsClose4H id={self.id}>"


class BBANDSStatsClose4H6Sl(StatsStrategy, Base):
    __tablename__ = "BBANDS_stats_close_4H_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSStatsClose4H id={self.id}>"


class BBANDSStatsClose1D0Sl(StatsStrategy, Base):
    __tablename__ = "BBANDS_stats_close_1D_0_0".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSStatsClose1D id={self.id}>"


class BBANDSStatsClose1D2Sl(StatsStrategy, Base):
    __tablename__ = "BBANDS_stats_close_1D_2_4".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSStatsClose1D id={self.id}>"


class BBANDSStatsClose1D4Sl(StatsStrategy, Base):
    __tablename__ = "BBANDS_stats_close_1D_4_8".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSStatsClose1D id={self.id}>"


class BBANDSStatsClose1D6Sl(StatsStrategy, Base):
    __tablename__ = "BBANDS_stats_close_1D_6_12".lower()
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<BBANDSStatsClose1D id={self.id}>"


class TradeHistoryBBANDS15T0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_bb_close_15T_0_0".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryBBANDS15T2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_bb_close_15T_2_4".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryBBANDS15T4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_bb_close_15T_4_8".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryBBANDS15T6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_bb_close_15T_6_12".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryBBANDS1H0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_bb_close_1H_0_0".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryBBANDS1H2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_bb_close_1H_2_4".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryBBANDS1H4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_bb_close_1H_4_8".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryBBANDS1H6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_bb_close_1H_6_12".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryBBANDS4H0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_bb_close_4H_0_0".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryBBANDS4H2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_bb_close_4H_2_4".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryBBANDS4H4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_bb_close_4H_4_8".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryBBANDS4H6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_bb_close_4H_6_12".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryBBANDS1D0Sl(Base, TradeHistory):
    __tablename__ = "trade_history_bb_close_1D_0_0".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryBBANDS1D2Sl(Base, TradeHistory):
    __tablename__ = "trade_history_bb_close_1D_2_4".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryBBANDS1D4Sl(Base, TradeHistory):
    __tablename__ = "trade_history_bb_close_1D_4_8".lower()
    id = Column(Integer, primary_key=True)


class TradeHistoryBBANDS1D6Sl(Base, TradeHistory):
    __tablename__ = "trade_history_bb_close_1D_6_12".lower()
    id = Column(Integer, primary_key=True)
