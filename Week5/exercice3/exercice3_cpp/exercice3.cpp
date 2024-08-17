#include <stdio.h>
#include <iostream>
#include <assert.h>
#include "circom.hpp"
#include "calcwit.hpp"
void BipartiteGraph2Coloring_0_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void BipartiteGraph2Coloring_0_run(uint ctx_index,Circom_CalcWit* ctx);
Circom_TemplateFunction _functionTable[1] = { 
BipartiteGraph2Coloring_0_run };
Circom_TemplateFunction _functionTableParallel[1] = { 
NULL };
uint get_main_input_signal_start() {return 2;}

uint get_main_input_signal_no() {return 20;}

uint get_total_signal_no() {return 85;}

uint get_number_of_components() {return 1;}

uint get_size_of_input_hashmap() {return 256;}

uint get_size_of_witness() {return 36;}

uint get_size_of_constants() {return 4;}

uint get_size_of_io_map() {return 0;}

void release_memory_component(Circom_CalcWit* ctx, uint pos) {{

if (pos != 0){{

if(ctx->componentMemory[pos].subcomponents)
delete []ctx->componentMemory[pos].subcomponents;

if(ctx->componentMemory[pos].subcomponentsParallel)
delete []ctx->componentMemory[pos].subcomponentsParallel;

if(ctx->componentMemory[pos].outputIsSet)
delete []ctx->componentMemory[pos].outputIsSet;

if(ctx->componentMemory[pos].mutexes)
delete []ctx->componentMemory[pos].mutexes;

if(ctx->componentMemory[pos].cvs)
delete []ctx->componentMemory[pos].cvs;

if(ctx->componentMemory[pos].sbct)
delete []ctx->componentMemory[pos].sbct;

}}


}}


// function declarations
// template declarations
void BipartiteGraph2Coloring_0_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 0;
ctx->componentMemory[coffset].templateName = "BipartiteGraph2Coloring";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 20;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[0];
}

void BipartiteGraph2Coloring_0_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[5];
FrElement lvar[5];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[0]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[1],&circuitConstants[0]); // line circom 10
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[1])) + 21)];
// load src
Fr_sub(&expaux[1],&circuitConstants[2],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[1])) + 17)]); // line circom 11
Fr_mul(&expaux[0],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[1])) + 17)],&expaux[1]); // line circom 11
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
Fr_add(&expaux[0],&lvar[1],&circuitConstants[2]); // line circom 10
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[1],&circuitConstants[0]); // line circom 10
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[1],&circuitConstants[0]); // line circom 18
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[2],&lvar[1]); // line circom 19
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &signalValues[mySignalStart + (((4 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[2]))) + 25)];
// load src
Fr_sub(&expaux[0],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[1])) + 17)],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[2])) + 17)]); // line circom 20
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + (((4 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[2]))) + 41)];
// load src
Fr_mul(&expaux[0],&signalValues[mySignalStart + (((4 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[2]))) + 1)],&signalValues[mySignalStart + (((4 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[2]))) + 25)]); // line circom 21
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + (((4 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[2]))) + 57)];
// load src
Fr_mul(&expaux[0],&signalValues[mySignalStart + (((4 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[2]))) + 41)],&signalValues[mySignalStart + (((4 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[2]))) + 41)]); // line circom 22
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
Fr_add(&expaux[0],&lvar[2],&circuitConstants[2]); // line circom 19
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[2],&lvar[1]); // line circom 19
}
{
PFrElement aux_dest = &lvar[1];
// load src
Fr_add(&expaux[0],&lvar[1],&circuitConstants[2]); // line circom 18
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[1],&circuitConstants[0]); // line circom 18
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[3]);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 73];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[2]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[2]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[0]); // line circom 34
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[2])) + 73)];
// load src
Fr_sub(&expaux[1],&lvar[2],&circuitConstants[2]); // line circom 36
Fr_sub(&expaux[2],&circuitConstants[2],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[3])) + 21)]); // line circom 36
Fr_mul(&expaux[0],&signalValues[mySignalStart + ((1 * Fr_toInt(&expaux[1])) + 73)],&expaux[2]); // line circom 36
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
Fr_add(&expaux[0],&lvar[2],&circuitConstants[2]); // line circom 37
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[4];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[4],&lvar[3]); // line circom 40
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[2])) + 73)];
// load src
Fr_sub(&expaux[1],&lvar[2],&circuitConstants[2]); // line circom 41
Fr_add(&expaux[3],&signalValues[mySignalStart + (((4 * Fr_toInt(&lvar[3])) + (1 * Fr_toInt(&lvar[4]))) + 57)],&circuitConstants[2]); // line circom 41
Fr_sub(&expaux[2],&expaux[3],&signalValues[mySignalStart + (((4 * Fr_toInt(&lvar[3])) + (1 * Fr_toInt(&lvar[4]))) + 1)]); // line circom 41
Fr_mul(&expaux[0],&signalValues[mySignalStart + ((1 * Fr_toInt(&expaux[1])) + 73)],&expaux[2]); // line circom 41
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
Fr_add(&expaux[0],&lvar[2],&circuitConstants[2]); // line circom 42
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[4];
// load src
Fr_add(&expaux[0],&lvar[4],&circuitConstants[2]); // line circom 40
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[4],&lvar[3]); // line circom 40
}
{
PFrElement aux_dest = &lvar[3];
// load src
Fr_add(&expaux[0],&lvar[3],&circuitConstants[2]); // line circom 34
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[0]); // line circom 34
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 0];
// load src
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + 83]);
}
for (uint i = 0; i < 0; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void run(Circom_CalcWit* ctx){
BipartiteGraph2Coloring_0_create(1,0,ctx,"main",0);
BipartiteGraph2Coloring_0_run(0,ctx);
}

