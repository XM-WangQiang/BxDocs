IO Map
======

====== =============== ====== === =========== ============== ======= ================
Name   Default         GPIO   CSC Special     Timer          ANAFunc PAD Connect
====== =============== ====== === =========== ============== ======= ================
PADA0  SWCLK,Pull-Down PA00   CSC SWCLK                      ADCIN0
PADA1  SWDIO,Pull-Up   PA01   CSC SWDIO       CTMR_ETR_IN(I) ADCIN1
PADA2  GPIO            PA02   CSC             CTMR_CH1(I/O)  ADCIN2  MICBIAS
PADA3  GPIO            PA03   CSC             CTMR_CH2(I/O)  MICIN
PADA4  GPIO            PA04   CSC             CTMR_CH3(I/O)  ADCIN3
PADA5  GPIO            PA05   CSC CLK_OUT(O)  CTMR_CH4(I/O)  ADCIN4
PADA6  GPIO,Pull-Up    PA06   CSC             ATMR_BK(I)     ADCIN5  DP
PADA7  GPIO,Pull-Up    PA07   CSC             ATMR_CH1P(I/O) ADCIN6  DM
PADA8  GPIO            PA08   CSC             ATMR_CH2P(I/O) ADCIN7
PADA9  GPIO            PA09   CSC             ATMR_CH3P(I/O) ADCIN8
PADA10 GPIO            PA10   CSC USB_DOP(O)  ATMR_CH4P(I/O) ADCIN9
PADA11 GPIO            PA11   CSC USB_DOM(O)  ATMR_CH1N(I/O) ADCIN0
PADA12 GPIO            PA12   CSC USB_NDOE(O) ATMR_CH2N(I/O) ADCIN1
PADA13 GPIO            PA13   CSC             ATMR_CH3N(I/O) ADCIN2
PADA14 GPIO            PA14   CSC             ATMR_ETR_IN(I) ADCIN4
PADA15 GPIO            PA15   CSC             CTMR_CH1(I/O)  ADCIN5
PADA16 GPIO            PA16   CSC             CTMR_CH2(I/O)  ADCIN6
PADA17 GPIO            PA17   CSC             CTMR_CH3(I/O)
PADA18 GPIO            PA18   CSC             CTMR_CH4(I/O)
PADA19 RST,Pull-Up     PA19   CSC
====== =============== ====== === =========== ============== ======= ================

说明:
    1. **Default** 为芯片上电IO默认功能.
    2. **GPIO** 为普通IO模式.
    3. **CSC** 为IO复用功能, 表示可以复用为UART/SPI/IIC/CTMR(CH1和CH2)的脚位功能.
    4. **Special** 为特殊功能, 其中PA05的CLK_OUT可以用来输出时钟.
    5. **Timer** 是固定IO. I表示输入, O表示输出.
    6. **ANAFunc** 为模拟功能, 主要是用于ADC. 注意PA03的模拟功能为语音输入.
    7. **PAD Connect** 为IO的物理连接, PA06和PA07可以配置为USB的DP和DM.