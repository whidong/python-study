import random
exp8 = f"{''}\u00B8"
problem_dict = {
    1: "What is the bit rate for the signal in the following fiqure?(첫 번째 과제 1번 그림참조)\n\n",
    2: "A non-preiodic composite signal contains frequencies fron 10 to 30KHz.\nThe peak amplitude is 10V for the lowest and the highest signals and is 30V for the 20KHz signal.\nAssuming that the amplitudes change gradually from the minimum to the maximum,\ndraw the frequency spectrum.\n\n",
    3: "The attenuation of a signal is -10dB.\n What is the final signal power if it was originally 5W?\n\n",
    4: "We measure the performance of a telephone line (4KHz of bandwidth).\nWhen the signal is 10V, the noise ifs 5mV.\nWhat is the maximum data rate supported by this telephone line?\n\n",
    5: "We need to upgrade a channel to a higher bandwidth. Answer the following questions.\n  a. How is the rate improved if we double the bandwidth?\n  b. How is the rate improved if we double the SNR?\n\n",
    6: f"What is the total delay for a frame of size 5 million bits that is being sent on a link with 10 routers each having\na queueing time of 2 micro seconds and a processing time of 1 micro seconds.\nThe length of the link is 2000km.\nThe speed of light inside the link is 2X10{exp8}m/s.\nThe link has bandwidth of 5Mbps.\nWhich component of the total delay is dominant?\nWhich one is negligible?\n\n",
    7: "근거리 통신망(LAN)은 _______로 정의된다.",
    8: "광역 통신망이 포괄할 수 있는 가장 큰 지역은 _____이다. \na. 마을\nb. 주\nc. 국가\nd. 세계",
    9: "제안 표준은 적어도 2개의 성공적인 시도 후 ____표준 상태로 올라간다.",
    10: "다음 중 데이토 통신시스템의 구성요소로 맞는것은?",
    11: "다음 중 데이터 통신 시스템의 특성으로 맞는 것은?",
    12: "______ 전송방식에서 데이터는 항상 한 방향으로만 전달된다.",
    13: "______ 전송방식에서 데이터는 항상 양방향으로만 전달된다.",
    14: "다음 중 네트워크 평가기준으로 맞는 것은?",
    15: "______ 통신에서 매체는 장치들 사이에 회선을 공유한다.",
    16: "______ 통신에서 통신 매체는 전용선이다.",
    17: "6대의 컴퓨터로 이루어진 성형 접속형태는 몇 개의 링크가 필요한가?",
    18: "RFC는 모든 인터넷 시스템으로 구현되어야 한다면 ______(으)로 분류된다.",
    19: " 원래 ARPANET에서 ______(은)는 직접 서로 연결되었다.",
    20: "______ 은(는) 보안 기능이 없는 회선으로 미국 내의 전산학과가 개설된 대학들을 연결하기 위해 구성되었다.",
    21: "현재 ______은(는) 인터넷 도메인 이름과 주소의 관리에 대한 책임이 있다.",
    22: "다음 중 데이터 통신 시스템의 구성요소가 아닌 것은?",
    23: "데이터 통신 시스템에서 ______은(는) 메시지가 전달되는 물리적인 경로이다.",
    24: "컴퓨터 본체와 키보드(자판)사이의 통신은 _____통신이다.",
    25: "텔레비전 방송은 ______전송의 예이다.",
    26: "______전송에서는 채널 욜량은 항상 통신하는 두 장치에 의해 공유된다.",
    27: "데이터 전송 방식에서 두 장치 간에 데이터 흐름 방향은 ______방식으로 일어날 수 있다.",
    28: "______전송 방식에서 데이터는 항상 한 방향으로만 전달한다.",
    29: "______전송 방식에서 데이터는 항상 동시에 양방향으로 전달된다.",
    30: "______통신 시스템이 고장 난 이후의 네트워크 복구 시간은 네트워크의 ______을 나타내는 측정치이다.",
    31: "권한을 가지지 않은 사용자는 네트워크 ______문제이다.",
    32: "다음 중 네트워크 평가기준이 아닌 것은?",
    33: "회선구성(Line Configuration)에서 ______연결은 두 장치 사이에 전용 회선을 제공한다.",
    34: "회선 구성에서 ______연결에서는 둘 또는 그 이상의 장치가 하나의 회선을 공유한다.",
    35: "______연결에서 오직 두 개의 장치만이 전용 링크에 의해 연결된다.",
    36: "______연결에서 세 개 또는 그 이상의 장치가 회선을 공유한다.",
    37: "______통신에서 전송매체는 장치들 사이에 회선을 공유한다.",
    38: "______통신에서 전송 매체는 전용선이다.",
    39: "다음 중 어느 접속형태가 중앙 제어 장치 또는 허브를 요구하는가?",
    40: " 데이터 통신 장치들은 ______접속형태로 연결될 수 있다.",
    41: "______은 네트워크의 물리적 또는 논리적인 구성을 말한다.",
    42: "______은 한 개의 건물, 공장 또는 캠퍼스 안에서나 또는 건물 사이에서 사용되는 데이터 통신 시스템이다.",
    43: "______은 국가 간 또는 전 세계를 연결하는 데이터 통신 시스템이다.",
    44: "광역 통신망(WAN)이 담당할 수 있는 가장 큰 지역은 ______이다.",
    45: "원래의 ARPANET에서는 ______은 직접 연결되었다.",
    46: "다음 중 세게 최초의 네트워크는?",
    47: "인터넷 서비스 제공업자에는 ______가 있다",
    48: "프로토콜에서 ______은 데이터가 어떤 순서로 표현되는지에 대한 데이터의 구조 또는 형식을 규정한다.",
    49: "프로토콜에서 ______은 특정 패턴이 어떻게 해석되어야 하는지를 규정하고 그 해석에 따라 어떤 동작이 취해져야 하는지를 규정한다.",
    50: "프로토콜에서 ______은 언제 데이터가 보내져야 되고 얼마나 빠르게 보내져야 되는지의 두 가지 특성을 지칭한다.",
    51: "______은 데이터 통신을 관장하는 일련의 규칙이다.",
    52: "다음 중 어떤 표준기관이 미국의 통신분야에 있어 국내 및 국제 교역에 대한 권한이 있는가?",
    53: "______들은 기업과 대학, 사용자와 공동 작업을 통하여 새로운 기술을 신속히 시험하고 평가하고 표준화하는 기관이다.",
    54: "다음 중 물리적인 연결에 대한 인터페이스와 전기 신호 규격을 개발하는 표준기관은?",
    55: "______은 현재 인터넷(Internet)의 프로토콜 집합이다.",
    56: "원래 ARPANET에서 ______은(는) 직접 서로 연결되었다.",
    57: "다음 중 전세계 각국의 학자들과 전문기술자들로 구성된 세계 최대 규모의 전기, 전자, 전기통신, 컴퓨터 분야의 전문 공학 학회로서 LAN 표준 개발로 알려진 기구는?",
    58: "데이터 통신 시스템의 다섯 가지 구성요소에 대해 설명하라.",
    59: "효율적이고 효과적인 네트워크를 위해 필요한 세 가지 평가기준(Criteria)은 무엇인가?",
    60: "점-대-점(Point-to-Point) 연결에 비해 다중점(Multipoint) 연결의 장점은 무엇인가?",
    61: "회선 구성(또는 연결 유형)의 두 가지 유형은 무엇인가?",
    62: "4가지 기본 네트워크 접속형태를 회선 구성에 따라 분류하라.",
    63: "반이중(Half-Duplex)방식과 전이중(Full-Duplex)방식의 차이는 무엇인가?",
    64: "4가지 기본 접속형태(Topology)를 열거하고 각 방식의 장점을 기술하라",
    65: "n개의 장치가 있는 네트워크에서 그물형, 링형, 버스형 그리고 성형 접속형태에 대해 각각 요구되는 케이블의 수는?",
    66: "데이터 통신 시스템에서 LAN이나 WAN으로 결정짓는 요소들은 무엇인가?",
    67: "인터넷(internet)과 인터넷(Internet)은 어떻게 서로 다른가?",
    68: "통신 시스템에서 왜 프로토콜(Protocol)이 필요한가?",
    69: "LAN의 링크 계층 교환기에서 HOST1은 HOST3에게 메시지를 전달하려 한다. 링크 계층 교환기를 통해 통신을 하는데, 교환기는 주소를 가질 필요가 있는가? 그 이유를 설명하라.",
    70: "만약 각 LAN이 다른 LAN들과 직접 통신해야 한다면 점-대-점(point-to-point) WAN에서는 몇 개의 연결(n개의 LAN)이 필요한가?",
    71: "지역 전화기를 사용하여 친구와 통화를 할 때, 회선-교환망(circuit-switched network)과 패킷-교환망(packet-switched network) 중 어느 것을 사용하는가?",
    72: "가입자가 전화 정보(dial-up) 서비스 또는 디지털 가입자 회선(DSL) 서비스를 이용하여 인터넷에 접속하려 할 때, 전화 회사의 역할은 무엇인가?",
    73: "양방향(Bidirectional)통신을 만들기 위해 필요한 프로토콜 계층화의 첫 번째 원칙은 무엇인가?",
    74: "인터넷 초안(Internet Draft)과 제안 표준(Proposal Standard) 간의 차이를 설명하라.",
    75: "요구(Required) RFC와 권고(Recommended) RFC간의 차이를 설명하라.",
    76: "IETF와 IRTF 임무 간의 차이를 설명하라.",
    77: "왜 표준(Standard)이 필요한가?",
    78: "성형 백본과 3개의 링형 네트워크를 연결한 혼합형 접속형태를 그림으로 그려라.",
    79: "링형 백본과 2개의 버스 네트워크를 연결한 혼합형 접속형태를 그림으로 그려라.",
    80: "Find the 8-bit data stream for each case depicted in the following fiqure.(2번째 과제 첫번째 그림 참조)\n\n",
    81: "The input stream to a 4B/5B block encoder is 0100 0000 0000 0000 0000 0001. Answer the following questions.\n  a) What is the output stream?\n b) What is the length of the longest consecutive sequence of 0s in the input?\n c) What is the length of the longest consecutive sequence of 0s in the output?\n\n",
    82: "What is the maximum data rate of a channel with a bandwidth of 200kHz if we use four levels of digital signaling?\n\n",
    83: "An analog signal has a max frequency of 2kHz. If we sample this signal and send it through a 20kbps channel, What is the SNR_dB?",
    84: "We want to transmit 1,000 characters with each character encoded as a8 bits.\n a) Find the number of transmitted bits for synchronous transmission.\n b) Find the number of transmitted bits for asynchronous transmission.\n c) Find the redundancy percent in each case.\n\n",
    85: "TCP/IP프로토콜은 ______개의 계층으로 구성되어 있다.\na. 2\nb. 3\nc. 5\nd. 6",
    86: "라우터는 TCP/IP 프로토콜 그룹의 _____계층을 포함하고 있다.\na. 2\n b. 3\nc. 4\nd. 5",
    87: "링크 계층 교환기는 TCP/IP 프로토콜 그룹의 ______계층에 속해있다.",
    88: "TCP/IP 프로토콜 그룹에서 다음 중 응용층 프로토콜은?",
    89: "TCP/IP 프로토콜 그룹에서 다음 중 전송층 프로토콜은?",
    90: "TCP/IP 프로토콜 그룹에서 다음 중 네트워크층 프로토콜은?",
    91: "TCP/IP 프로토콜 그룹에서 전송층 패킷은 ______(이)라 불린다.",
    92: "TCP/IP 프로토콜 그룹에서 ______계층은 하나의 홉(노드)에서 다음 홉으로 프레임 전달에 대한 책임이 있다.",
    93: "TCP/IP 프로토콜 그룹에서 물리층은 물리적인 매체를 통해 ______의 전달에 책임이 있다.",
    94: "TCP/IP 프로토콜 그룹에서 포트 번호는 ______에서 사용하는 식별자이다.",
    95: "TCP/IP 프로토콜 그룹에서 논리 주소는 ______에서 사용하는 식별자이다.",
    96: "______계층은 하난의 프로세스에서 다른 프로세스로 메시지 전송에 대한 책임이 있다.",
    97: "인터넷 프로토콜(IP)는 ______프로토콜이다.",
    98: "TCP/IP 프로토콜 그룹에서 응용층은 일반적으로 OSI모델에서 ______계층의 조합으로 간주한다.",
    99: "TCP/IP에서 응용층에 있는 메시지는 계층의 패킷에 캡슐화된다.",
    100: "TCP/IP에서 전송층에 있는 메시지는 ______계층의 패킷에 캡슐화 된다.",
    101: "TCP/IP에서 네트워크층에 있는 메시지는 ______계층의 패킷으로부터 역캡슐화된다.",
    102: "TCP/IP에서 전송층에 있는 메시지는 ______계층의 패킷으로부터 역탭슐화된다.",
    103: "TCP/IP에서 네트워크층 개체의 논리적인 연결은 또 다른 ______계층의 개체와 이루어진다.",
    104: "TCP/IP에서 데이터 링크층 개체의 논리적인 연결은 또 다른 ______계층의 개체와 이루어진다.",
    105: "TCP/IP에서 3계층의 패킷은 ______ 계층의 데이터와 ______계층의 헤더를 전달한다.",
    106: "TCP/IP 프로토콜 중 어떤 계층들이 링크층 교환기에 포함되는가?",
    107: "1개의 라우터가 3개의 링크(네트워크)에 연결되어 있다. 다음 각 계층에는 얼마나 많은 라우터들이 관련되어 있는가?\na. 물리층\nb. 데이터 링크층\nc. 네트워크 층",
    108: "TCP/IP 프로토콜에서 응용층의 논리적인 연결을 생각할 때 송신자와 수신자 입장에서 동일한 객체는 무엇인가?",
    109: "어떤 호스트가 TCP/IP 프로토콜을 이용하여 다른 호스트와 통신을 수행한다. 다음 각 계층에서 송수신된 데이터 단위는 무엇인가?\na. 응용층\nb. 네트워크층\nc. 데이터 링크층",
    110: "다음 데이터 단위 중 어떤 것이 프레임에 캡슐화되는가?\na. 사용자 데이터그램\nb. 데이터그램\nc. 세그먼트",
    111: "다음 데이터 단위 중 어떤 것이 사용자 다이어그램으로부터 역캡슐롸가 된 것인가?\na. 데이터그램\nb. 세그먼트\nc. 메시지",
    112: "다음 데이터 단위 중 어느 것이 4계층으로부터 헤더가 추가된 응용층 메시지를 갖는가?\na. 프레임\nb. 데이터그램\nc. 비트",
    113: "응용층 프로토콜의 몇 가지를 나영하라.",
    114: "만약 포트 번호가 16비트(2바이트)라면, TCP/IP 프로토콜의 전송층에서 최소 헤더 크기는 얼마인가?",
    115: "다음 계층에서 사용되는 주소(식별자)의 유형은 무엇인가?\na. 응용층\nb. 네트워크층\nc. 데이터 링크층",
    116: "전송층의 응용층 메시지에 대한 다중화(multiplex)와 역다중화(demultiplex)를 언급할 때, 전송층 프로토콜의 한 패킷이 응용층으로부터 몇 개의 메시지를 결합할 수 있음을 의미하는가? 이유를 설명하라.",
    117: "각 호스트의 연결을 위해 2개의 독립된 호스트를 함께 연결하고자 한다고 가정하자. 두 호스트 간 링크층 교환기가 필요한가?",
    118: "만약 발신지 호스트와 목적지 호스트 사이에 단일 경로가 있다면, 두 호스트 사이에 라우터가 필요한가?",
    119: "주파수 영역 도면에서 수평선은 ______이다\na. 신호의 진폭\nb. 주파수\nc. 위상\nd. 시간",
    120: "시간 영역 도면에서 수평선은 ______이다.\na. 신호의 진폭\nb. 주파수\nc. 위상\nd. 시간",
    121: "데이터를 전송하기 전에 데이터를 ______로 변환해야 한다.\na. 주기신호\nb. 전자기신호\nc. 비주기신호\nd. 저주파 정현파",
    122: "어떤 주기 신호는 0.001초 만에 한 사이클을 완성한다. 주파수는 얼마인가?\na. 1Hz\nb. 100Hz\nc. 1kHz\nd. 1MHz",
    123: "______데이터는 연속적이고 연속적인 값을 갖는다.",
    124: "______데이터는 이산 상태를 가지며 이산 값을 갖는다.",
    125: "______신호는 시간 간격에서 무한개수의 값을 가질 수 있다.",
    126: "______신호는 시간 간격에서 한정된 수의 값만 가질 수 있다.",
    127: "주파수와 주기는 ______의 관계를 가진다",
    128: "______은 시간에 대한 변화율이다.",
    129: "______는 시간 0에 대한 상대적인 파형의 위치를 나타낸다.",
    130: "단순 정현파는 ______영역에서는 단 하나의 막대로 나타낼 수 있다.",
    131: "주파수가 높아짐에 따라 주기는 ______한다",
    132: "______는 신호가 전송매체의 저항 때문에 신호의 강도를 잃어버리는 전송 장애의 한 종류이다.",
    133: "______은 신호를 구성하는 각 주파수의 전파 속도 차이로 인해 신호의 강도를 잃어버리는 전송 장애의 한 종류이다.",
    134: "______는 교차 잡음과 같이 외부 신호로 인해 생기는 전송 장애의 한 종류이다.",
    135: "전파 속도를 전파 시간으로 곱하면 ______을 얻는다.",
    136: "디지털 신호의 기저대역 전송은 ______채널을 사용할 때만 가능하다.",
    137: "이용 가능한 채널이 ______채널이면 채널에 직접 디지털 신호를 정송할 수 없다.",
    138: "______채널에서는 나이퀴스트 비트 정송률 공식이 최대 비트 정송률을 결정한다.",
    139: "______채널에서는 최대 비트 정송률을 알기 위해서는 섀넌 용량을 사용해야 한다.",
    140: "______는 신호를 망가뜨릴 수 있다.",
    141: "______ 곱은 링크를 채울 수 있는 비트 수를 결정한다.",
    142: "주기와 주파수의 관계는 무엇인가?",
    143: "신호의 진폭은 무엇을 측정하는가?\n신호의 주파수는 무엇을 측정하는가?\n신호의 위상은 무엇을 측정하는가?",
    144: "복합 신호는 어떻게 개별적인 주파수로 분해되는가?",
    145: "전송 장애의 세 가지 유형을 기술하라.",
    146: "기저대역 전송과 광대역 전송을 구별하라.",
    147: "나이퀴스트 정리와 통신의 관계는 무엇인가?",
    148: "섀넌 용량과 통신의 관계는 무엇인가?",
    149: "광섬유에 사용되는 광신호는 왜 짧은 파장을 갖는가?",
    150: "주파수 영역 도면을 보고 신호가 주기적인지 비주기적인지 알 수 있는가?",
    151: "음성 신호를 주파수 영역 도면으로 나타내면 이산적인가 연속적인가?",
    152: "알람 시스템을 주파수 영역 도면으로 나타내면 이산적인가 연속적인가?",
    153: "마이크로폰에서 음성신호를 녹음기로 보낸다. 기저대역 전송인가 광대역 전송인가?",
    154: "LAN의 한 지점에서 다른 지점으로 디지털 신호를 보낸다. 기저대역 전송인가 광대역 전송인가?",
    155: "여러 개의 음성 신호를 변조하여 공기를 통해 보낸다. 기저대역 전송인가 광대역 전송인가?",
    156: "극형과 양극형 부호화는 ______ 부호화의 유형이다.",
    157: "______변환은 회선 부호화, 블록 부호화 및 뒤섞기 기술을 모두 사용한다.",
    158: "______방식에서는 전압은 음과 양이 된다. 예를 들면 0을 위한 전압은 1을 위한 전압이 음이 되는 경우에는 양이 될 수 있다.",
    159: "______에서는 전압의 준위가 비트의 값을 결정한다.",
    160: "______에서는 전압 준위가 변화하거나 변화하지 않는 것으로 비트의 값을 결정한다.",
    161: "RZ의 아이디어와 NRZ-L의 아이디어를 합한 것이 ______이다.",
    162: "RZ의 아이디어와 NRZ-I의 아이디어를 합한 것이 ______이다.",
    163: "맨체스터 부호화와 차분 맨체스터 부호화에서 비트의 중간 지점에서의 전이는 ______에 사용된다.",
    164: "______ 부호화에서는 양, 영 및 음이라는 3개의 준위를 사용한다.",
    165: "______ 방식은 2비트 데이터 크기를 4준위 신호 중 하나에 속하는 2비트 패턴의 1개 신호요소로 부호화한다.",
    166: "______ 부호화는 각 비트의 중간에서 전이를 갖는다.",
    167: "______ 부호화는 각 0비트가 시작할 때 전이를 갖는다.",
    168: "다음 중 동기화를 제공하지 않는 부호화 방법은?\na. NRZ-L\nb. RZ\nc. NRZ-I\nd. 맨체스터",
    169: "다음 중 1을 나타내기 위해 양과 음의 값을 번갈아 사용하는 부호화 방법은?\na. NRZ-I\nb. RZ\nc. 맨체스터\nd. AMI",
    170: "블록 부호화는 수신자 측에서 ______하는 것을 돕는다.",
    171: "______은 디지털 데이터를 디지털 신호로 변환하는 과정이다.",
    172: "______는 동기화와 오류검출을 위해 중복 비트를 제공한다.",
    173: "______은 보통 mB/nB 부호화로 불리는데 각m개 비트 그룹을 n개 비트 그룹으로 대체한다.",
    174: "______은 비트 수를 늘리지 않고 동기화를 제공한다.",
    175: "두 가지 널리 사용되는 뒤섞기에는 ______이 있다.",
    176: "PCM은 ______ 변환의 예이다.",
    177: "아날로그 신호를 디지털 데이터로 변환하는 가장 흔한 기법은 ______(이)라 불린다.",
    178: "PCM의 제 1단계는 ______이다.",
    179: "______은 각 표본의 신호 진폭 값을 찾으며, ______은 직전 표본 값과의 차이를 찾는다.",
    180: "디지털-대-디지털 변환의 세가지 기법을 기술하라.",
    181: "신호 요소와 데이터 요소의 차이를 설명하라",
    182: "데이터율과 신호율의 차이를 설명하라.",
    183: "기준선 표류를 정의하고 디지털 전송에서 그 영향을 기술하라.",
    184: "DC의 성분은 무엇이며, 디지털 전송에서의 영향은?",
    185: "자기 동기화 신호의 특징을 기술하라.",
    186: "5가지 회선 부호화 방식을 적어라.",
    187: "블록 부호화를 정의하고, 그 목적을 기술하라.",
    188: "뒤섞기(scrambling)을 정의하고 그 목적을 기술하라.",
    189: "PCM과 DM을 비교하고 설명하라.",
    190: "병렬 전송과 직렬 전송의 차이점은 무엇인가?",
    191: "직렬 전송의 3가지 기법을 적고, 그 차이를 설명하라."
    }

def printProblem():
    n = 1
    doublecheck = []
    print(" y 또는 n을 입력하세요.")
    while True:
        rand = random.randint(1, 191)
        cmd = input()
        if cmd == 'n':
            print("\n프로그램을 종료합니다.")
            return None
        elif cmd == 'y' and cmd not in doublecheck:
            print(f"다음은 {n}번째 문제입니다.\n")
            print(problem_dict[rand] + "\n")
            n += 1
            doublecheck.append(rand)
        else:
            print("잘못된 입력입니다.\n올바른 입력을 해주세요.\n허용된 입력어는 'Yes'아니면 'No'입니다.")

excute = printProblem()
print(excute)