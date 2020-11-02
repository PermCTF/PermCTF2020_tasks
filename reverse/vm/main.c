#include <cstdio>
#include <cstring>

#define STACK_SIZE 20
#define KEY_SIZE 50


enum OPCODE { ADD, EXIT, NOP, SUB, INC, INCS, DEC, XOR, PUSH, POP, MOV, MOVS, LOOP, CMP, CMPR, JL, JG, JZ };

struct R {
	unsigned int r0;
	unsigned int r1;
	unsigned int rcx;
  unsigned char *s;
	signed int zf;   //Con flag
	unsigned char *rsp;  //SP
	unsigned char *rip; //IP
};

class VM {
private:
	struct R r;
	virtual void vmc_nop();
	virtual void vmc_add();
	virtual void vmc_sub();
	virtual void vmc_inc();
	virtual void vmc_dec();
	virtual void vmc_xor();
	virtual void vmc_push();
	virtual void vmc_pop();
	virtual void vmc_mov();
	virtual void vmc_loop();
	virtual void vmc_cmp();
	virtual void vmc_cmpr();
	virtual void vmc_jl();
	virtual void vmc_jg();
	virtual void vmc_jz();
	virtual void vmc_incs();
	virtual void vmc_movs();

public:
#ifdef DEBUG
	virtual void vm_debug();
#endif
	virtual int vm_init(R *in);
	virtual void vm_out(R *out) const;
	virtual void vm_cycle();
	virtual unsigned int* vmc_getreg(unsigned char value);
};

#ifdef DEBUG
void VM::vm_debug() {
  static int count = 0;
	printf("DEBUG: count: %i \nR0 = %x %x\nR1 = %x %x\nRCX = %x %x\nZF = %x\nRSP = %x\nRIP = %x\n", count, r.r0, &r.r0, r.r1, &r.r1, r.rcx, &r.rcx, r.zf, r.rsp, r.rip);
  printf("RIP now: %x, RIP next: %x \n",r.rip, (r.rip+3));
  printf("STACK:\n");
  for(int i=0;i<STACK_SIZE;i++) {
    printf("%i: %x -  %x\n", i,r.rsp+i,*(r.rsp+i));
  }
  count++;
}
#endif


int VM::vm_init(R *in) {
#ifdef DEBUG
	printf("%s", "VM::vm_init\n");
#endif
	r.r0 = in->r0;
	r.r1 = in->r1;
	r.zf = 0;
	r.rcx = 0;
	r.rsp = in->rsp;
	r.rip = in->rip;
  r.s = in->s;
	return 0;
}

void VM::vm_out(R *out) const {
#ifdef DEBUG
	printf("%s", "VM::vm_out\n");
#endif
	out->r0 = r.r0;
	out->r1 = r.r1;
	out->zf = r.zf;
  out->s = r.s;
	out->rcx = r.rcx;
	out->rsp = r.rsp;
	out->rip = r.rip;
}

unsigned int* VM::vmc_getreg(unsigned char value) {
	switch(value) {
  case 0x00:
    return &r.r0;
  case 0x01:
      return &r.r1;
  case 0x02:
      return &r.rcx;
  }
  return &r.r0;
}

void VM::vmc_nop() {
	r.rip += 3;
#ifdef DEBUG
	printf("%s", "NOP\n");
#endif
}

void VM::vmc_add() {
  unsigned int *reg  = vmc_getreg(*(r.rip+1));
	int value = *(r.rip + 2);
	*reg = *reg + value;
	r.rip += 3;
#ifdef DEBUG
  printf("ADD REG: %x VALUE: %i\n", reg, value);
	vm_debug();
#endif
}

void VM::vmc_sub() {
  unsigned int *reg  = vmc_getreg(*(r.rip+1));
	int value = *(r.rip + 2);
	*reg = *reg - value;
	r.rip += 3;
#ifdef DEBUG
  printf("SUB REG: %x VALUE: %i\n", reg, value);
	vm_debug();
#endif
}


void VM::vmc_inc() {
  unsigned int *reg  = vmc_getreg(*(r.rip+1));
	*reg++;
	r.rip += 3;
#ifdef DEBUG
  printf("INC REG: %x\n", reg);
	vm_debug();
#endif
}

void VM::vmc_incs() {
  r.s++;
  r.rip +=3;
#ifdef DEBUG
  printf("INC REGs: %x\n", r.s);
	vm_debug();
#endif
}

void VM::vmc_dec() {
  unsigned int *reg  = vmc_getreg(*(r.rip+1));
	*reg--;
	r.rip += 3;
#ifdef DEBUG
  printf("DEC REG: %x\n", reg);
	vm_debug();
#endif
}

void VM::vmc_xor() {
	unsigned int *reg  = vmc_getreg(*(r.rip+1));
	int value = *(r.rip + 2);
	*reg = *reg ^ value;
	r.rip += 3;
#ifdef DEBUG
  printf("XOR REG: %x VALUE: %i\n", reg, value);
	vm_debug();
#endif
}


void VM::vmc_push() {
	unsigned int *reg  = vmc_getreg(*(r.rip+1));
	r.rsp -= 1;
  *r.rsp = *reg;
	r.rip += 3;
#ifdef DEBUG
	printf("PUSH %x VALUE: %02x\n",reg,*reg );
	vm_debug();
#endif
}


void VM::vmc_pop() {
	unsigned int *reg  = vmc_getreg(*(r.rip+1));
  *reg = *r.rsp;
	r.rsp += 1;
	r.rip += 3;
#ifdef DEBUG
	printf("POP %x VALUE: %i\n", reg, *reg);
	vm_debug();
#endif
}

void VM::vmc_mov() {
	unsigned int *reg  = vmc_getreg(*(r.rip+1));
	int value = *(r.rip + 2);
  *reg = value;
	r.rip += 3;
#ifdef DEBUG
	printf("MOV R %x, Value: %i\n", reg, value);
	vm_debug();
#endif
}

void VM::vmc_movs() {
	unsigned int *reg  = vmc_getreg(*(r.rip+1));
	char value = *(r.s);
  *reg = (unsigned int) value;
	r.rip += 3;
#ifdef DEBUG
	printf("MOV R%x, Value: %x\n", reg, value);
	vm_debug();
#endif
}


void VM::vmc_loop() {
  int value = *(r.rip + 1);
  r.rcx -=1;
  if (r.rcx != 0) {
    r.rip -= value*3;
  }
	r.rip += 3;
#ifdef DEBUG
	printf("LOOP -%i RCX: %i\n", value, r.rcx);
  vm_debug();
#endif
}

void VM::vmc_cmp() {
	unsigned int *reg  = vmc_getreg(*(r.rip+1));
	int value = *(r.rip + 2);
  if (*reg > value) {
    r.zf = 1;
  }
  else if (*reg < value) {
    r.zf = -1;
  }
  else {
    r.zf = 0;
  }
	r.rip += 3;
#ifdef DEBUG
	printf("CMP R %x, Value: %02x\n", reg, value);
	vm_debug();
#endif
}

void VM::vmc_cmpr() {
	unsigned int *reg  = vmc_getreg(*(r.rip+1));
	unsigned int *reg2  = vmc_getreg(*(r.rip+2));
  if (*reg > *reg2) {
    r.zf = 1;
  }
  else if (*reg < *reg) {
    r.zf = -1;
  }
  else {
    r.zf = 0;
  }
	r.rip += 3;
#ifdef DEBUG
	printf("CMPR R %x, R %02x\n", reg, reg2);
	vm_debug();
#endif
}

void VM::vmc_jl() {
	int value = *(r.rip + 1);
	if (r.zf == -1) {
		r.rip += value*3;
	}
	else {
		r.rip += 3;
	}
#ifdef DEBUG
	if (r.zf == -1)
		printf("JL +%X (JUMPED)\n", value);
	else
		printf("JL (NOT JUMPED)\n");
	vm_debug();
#endif
}

void VM::vmc_jg() {
	int value = *(r.rip + 1);
	if (r.zf == 1) {
		r.rip += value*3;
	}
	else {
		r.rip += 3;
	}
#ifdef DEBUG
	if (r.zf == 1)
		printf("JG +%X (JUMPED)\n", value);
	else
		printf("JG (NOT JUMPED)\n");
	vm_debug();
#endif
}

void VM::vmc_jz() {
	int value = *(r.rip + 1);
	if (r.zf == 0) {
		r.rip += value*3;
	}
	else {
		r.rip += 3;
	}
#ifdef DEBUG
	if (r.zf == 0)
		printf("JZ +%X (JUMPED)\n", value);
	else
		printf("JZ (NOT JUMPED)\n");
	vm_debug();
#endif
}

void VM::vm_cycle() {
#ifdef DEBUG
    printf("%s", "VM::vm_run\n");
	vm_debug();
#endif
	while (1) {
		unsigned char *command = r.rip;
#ifdef DEBUG
		printf("OPCODE: %02X\n", *command);
#endif
		switch (*command) {
		case EXIT:
			goto exit;
		case ADD:
			vmc_add();
			break;
		case SUB:
			vmc_sub();
			break;
		case INC:
			vmc_inc();
			break;
		case DEC:
			vmc_dec();
			break;
		case XOR:
			vmc_xor();
			break;
		case PUSH:
			vmc_push();
			break;
		case POP:
			vmc_pop();
			break;
		case MOV:
			vmc_mov();
			break;
		case LOOP:
			vmc_loop();
			break;
		case CMP:
			vmc_cmp();
			break;
		case CMPR:
			vmc_cmpr();
			break;
		case JL:
			vmc_jl();
			break;
		case JG:
			vmc_jg();
			break;
		case JZ:
			vmc_jz();
			break;
		case INCS:
			vmc_incs();
			break;
		case MOVS:
			vmc_movs();
			break;
		default:
      printf("nop");
			vmc_nop();
		}
}
#ifdef DEBUG
	printf("%s", "VM::END\n");
#endif
exit:
	return;
}



unsigned char CODE[] =
{
  MOV, 0x00, 0xF1,
  PUSH, 0x00, 0x00, //some keys
  MOV, 0x00, 0xE6,
  PUSH, 0x00, 0x00, //some keys
  MOV, 0x00, 0xE5,
  PUSH, 0x00, 0x00, //some keys
  MOV, 0x00, 0xE4,
  PUSH, 0x00, 0x00, //some keys
  MOV, 0x00, 0xEB,
  PUSH, 0x00, 0x00, //some keys
  MOV, 0x00, 0xA0,
  PUSH, 0x00, 0x00, //some keys
  MOV, 0x00, 0xE9,
  PUSH, 0x00, 0x00, //some keys
  MOV, 0x00, 0xF5,
  PUSH, 0x00, 0x00, //some keys
  MOV, 0x00, 0xE5,
  PUSH, 0x00, 0x00, //some keys
  MOV, 0x00, 0xDE,
  PUSH, 0x00, 0x00, //some keys

  MOV, 0x02, 0x05,

  MOVS, 0x00, 0x00, //input cycle

  CMP, 0x00, 0x2f,
  JG, 0x02, 0x00,
  EXIT, 0x00, 0x00,
  CMP, 0x00, 0x7c,
  JL, 0x02, 0x00,
  EXIT, 0x00, 0x00,

  POP, 0x01, 0x00, //odd
  XOR, 0x00, 0xBB,
  ADD, 0x00, 0x11,
  CMPR, 0x00, 0x01,
  JZ, 0x02, 0x00,
  EXIT, 0x00, 0x00,
  INCS, 0x00, 0x00,

  MOVS, 0x00, 0x00,

  CMP, 0x00, 0x2f,
  JG, 0x02, 0x00,
  EXIT, 0x00, 0x00,
  CMP, 0x00, 0x7c,
  JL, 0x02, 0x00,
  EXIT, 0x00, 0x00,

  POP, 0x01, 0x00, //even
  XOR, 0x00, 0xAA,
  ADD, 0x00, 0x22,
  CMPR, 0x00, 0x01,
  JZ, 0x02, 0x00,
  EXIT, 0x00, 0x00,
  INCS, 0x00, 0x00,

  LOOP, 0x1D, 0x00,

  MOVS, 0x00, 0x00,
  CMP, 0x00, 0x00,
  JZ, 0x02, 0x00,
  EXIT, 0x00, 0x00,
  MOV, 0x00,0x13,
  EXIT, 0x00,0x00,

};

int main(int argc, char *argv[]) {
	if (argc < 2) {
		printf("Provide key as argument\n");
		return 0;
	}
	VM *vm = new VM;
	R *x = new R;
	x->r0 = 0;
	x->r1 = 0;

	unsigned char *input = new unsigned char[KEY_SIZE];
	unsigned char *stack = new unsigned char[STACK_SIZE];

	memcpy(input, argv[1], KEY_SIZE);
	x->s = input;
	x->rsp = stack+STACK_SIZE-1;
	x->rip = CODE;
	vm->vm_init(x);
	vm->vm_cycle();
	vm->vm_out(x);
	if (x->r0 == 0x13) {
		printf("Right\n");
	}
	else {
		printf("Wrong\n");
	}
	delete[] stack;
	delete[] input;
	delete x;
	delete vm;
	return 0;
}

