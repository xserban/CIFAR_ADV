import torch
from torchvision import datasets, transforms

mean = (0.4914, 0.4822, 0.4465)
std = (0.2471, 0.2435, 0.2616)


def get_datasets(flag, dir, batch_size):
    t_trans, tst_trans = get_transforms()
    if flag == "10":
        num_workers = 2
        train_dataset = datasets.CIFAR10(
            dir, train=True, transform=t_trans, download=True)
        tst_dataset = datasets.CIFAR10(
            dir, train=False, transform=tst_trans, download=True)
        train_loader = torch.utils.data.DataLoader(
            dataset=train_dataset, batch_size=batch_size, shuffle=True, pin_memory=True, num_workers=num_workers)
        tst_loader = torch.utils.data.DataLoader(
            dataset=tst_dataset, batch_size=batch_size, shuffle=False, pin_memory=True, num_workers=2)
        return train_loader, tst_loader
    elif flag == "100":
        pass
    else:
        raise BaseException("Invalid dataset flag")


def get_transforms():
    train_transforms = transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)])
    test_transforms = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean, std)])
    return train_transforms, test_transforms