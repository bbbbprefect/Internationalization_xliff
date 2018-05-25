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
@property(strong,nonatomic)UIButton *btn2;
@property(strong,nonatomic)UIButton *btn3;

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    
    //#define NSLocalizedString(key, comment) \
    [NSBundle.mainBundle localizedStringForKey:(key) value:@"" table:nil]
    
    self.btn = [[UIButton alloc]initWithFrame:CGRectMake(60, 100, 80, 40)];
    [self.btn setTitle:NSLocalizedString(@"首页", @"首页") forState:UIControlStateNormal];
    self.btn.backgroundColor = [UIColor blueColor];
    [self.view addSubview:self.btn];
    
    self.btn2 = [[UIButton alloc]initWithFrame:CGRectMake(60, 200, 80, 40)];
    [self.btn2 setTitle:NSLocalizedString(@"今天", @"今天") forState:UIControlStateNormal];
    self.btn2.backgroundColor = [UIColor blueColor];
    [self.view addSubview:self.btn2];
    
    self.btn3 = [[UIButton alloc]initWithFrame:CGRectMake(60, 300, 80, 40)];
    [self.btn3 setTitle:NSLocalizedString(@"明天", @"明天") forState:UIControlStateNormal];
    self.btn3.backgroundColor = [UIColor blueColor];
    [self.view addSubview:self.btn3];
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


@end
