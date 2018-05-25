//
//  ViewController.m
//  InternDemo
//
//  Created by 赵祥 on 2018/5/14.
//  Copyright © 2018年 赵祥. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@property(strong,nonatomic)UIButton *btn;

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    
    self.btn = [[UIButton alloc]initWithFrame:CGRectMake(20, 20, 50, 20)];
    [self.btn setTitle:NSLocalizedString(@"首页", @"首页") forState:UIControlStateNormal];
    self.btn.backgroundColor = [UIColor blueColor];
    [self.view addSubview:self.btn];
    NSLocalizedString(@"今日", @"今日");
    NSLocalizedString(@"明天", @"明天");
    NSLocalizedString(@"后天", @"后天");
    NSLocalizedString(@"dahout", @"dahout");
    NSLocalizedString(@"zhaoxiang", @"zhaoxiang");
    NSLocalizedString(@"zhaozhao", @"zhaozhao");
    NSLocalizedString(@"xiangxiang", @"xiangxiang");
    NSLocalizedString(@"qqqqqqqqqq", @"qqqqqqqqqq");
    NSLocalizedString(@"大da后天", @"qqqqqqqqqq");
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


@end
